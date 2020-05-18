# -*- coding: utf-8 -*-
from openerp import _, api, models, fields

class StockPicking(models.Model):
    _inherit = "stock.picking"

    po_request_id = fields.Many2one('purchase.order', string="Purchase Order")

    @api.model
    def _purchase_request_picking_confirm_message_content(self, picking, request, request_dict):
        if not request_dict:
            request_dict = {}
        title = _('Receipt confirmation %s for your Request %s') % (picking.name, request.name)
        message = '<h3>%s</h3>' % title
        message += _('The following requested items from Purchase Request %s '
                     'have now been received in Incoming Shipment %s:') % (request.name, picking.name)
        message += '<ul>'
        for line in request_dict.values():
            message += _(
                '<li><b>%s</b>: Received quantity %s %s</li>'
            ) % (line['name'],
                 line['product_qty'],
                 line['product_uom'],
                 )
        message += '</ul>'
        return message

    @api.multi
    def do_transfer(self):
        super(StockPicking, self).do_transfer()
        request_obj = self.env['purchase.request']
        for picking in self:
            requests_dict = {}
            if picking.picking_type_id.code != 'incoming':
                continue
            for move in picking.move_lines:
                if move.purchase_line_id:
                    for request_line in move.purchase_line_id.purchase_request_lines:
                        request_id = request_line.request_id.id
                        if request_id not in requests_dict:
                            requests_dict[request_id] = {}
                        data = {
                            'name': request_line.name,
                            'product_qty': move.product_qty,
                            'product_uom': move.product_uom.name,
                        }
                        requests_dict[request_id][request_line.id] = data
            for request_id in requests_dict:
                request = request_obj.browse(request_id)
                message = self._purchase_request_picking_confirm_message_content(picking, request, requests_dict[request_id])
                request.message_post(body=message, subtype='mail.mt_comment')
            print picking
            print "------------"
            po_rec = picking.po_request_id or []
            if picking.state == 'done' and po_rec:
                for po_line_rec in po_rec.order_line or []:
                    for prl_rec in po_rec.purchase_rl_ids:
                        if po_line_rec.prl_id.id == prl_rec.prl_id.id:
                            prl_rec.prl_id.quantity_delivered = po_line_rec.qty_received or 0.0
StockPicking()

