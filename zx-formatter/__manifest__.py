# Part of pmis_ux odoo module. See README, manifest and
# LICENSE files for full copyright and licensing details.
{
    'name': 'en_US Formatter',
    'version': '12.0.1',
    'category': 'ZX-TEST',
    'license': 'AGPL-3',
    'author': 'Nejc86, '
              'Luxim, '
              'Matmoz, '
              'PMISuite',
    'website': 'https://luxim.si',
    'contributors': [
        'Matjaž Mozetič <matjaz@luxim.si>',
        'Devid Miklus <devid@luxim.si>',
        'Nejc Gale <nejc@luxim.si>',
    ],
    'depends': [
        'base'
        # 'sale_stock', # (included in sale_backorder)
        # 'purchase_stock', # (included in purchase_backorder)
        # 'sale_backorder',
        # 'purchase_backorder'
        # 'pmis_product_pricelist_supplierinfo'
    ],
    'data': [
        'data/reformat_leng.xml'
    ],
    'summary': 'en_US Formatter',
    'installable': True,
    'application': False,
    'auto_install': False,
}
