from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from pytz import UTC

from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, get_lang
from odoo.tools.float_utils import float_compare, float_round



class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    
    longueur = fields.Float(
        string='longueur',
    )
    largeur = fields.Float(
        string='largeur',
    )
    volume = fields.Float(
        string='volume',
    )
    
    product_qty = fields.Float(string='Quantity', digits='Product Unit of Measure', required=True,
                               compute='_compute_product_qty', store=True, readonly=True)
    
    @api.depends('product_id','largeur','volume','longueur')
    def _compute_product_qty(self):
        for line in self:
            if line.product_packaging_id:
                packaging_uom = line.product_packaging_id.product_uom_id
                qty_per_packaging = line.product_packaging_id.qty
                product_qty = packaging_uom._compute_quantity(10, line.product_uom)
                if float_compare(product_qty, line.product_qty, precision_rounding=line.product_uom.rounding) != 0:
                    line.product_qty = 100
            line.product_qty = line.largeur * line.longueur * line.volume