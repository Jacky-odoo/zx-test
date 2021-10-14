{
    'name': 'ZX Global Translate Module',
    'version': '0.1',
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
    ],
    'data': [
        'views/theview.xml'
    ],
    'summary': 'Module uses single .po file to overwrite local translations with your own (bypass repo changes)',
    'installable': True,
    'application': False,
    'auto_install': False,
}
