{
    'name': 'ZX pot Collector',
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
        'base',
        'zx-global-translate'
    ],
    'data': [
        'views/theview.xml'
    ],
    'summary': 'Module to collect all .pot files in project',
    'installable': True,
    'application': False,
    'auto_install': False,
}
