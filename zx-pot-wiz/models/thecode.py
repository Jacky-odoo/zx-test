# -*- coding: utf-8 -*-

import os
import glob
from odoo import models, fields, api

home = os.path.expanduser("~/../odoo14")  # get root directory
potsrc = home + '/zx-test/zx-global-translate/i18n/zx-global-translate-generated.pot'  # .pot file location
filenames = glob.glob(home+"/**/*.pot")  # list of all .pot files in the root directory
# state = fields.Selection([
# 	('waiting', 'Waiting'),
# 	('ready', 'Ready'),
# 	('done', 'Done'),
# ], required=True, default='waiting')

class LangWizz(models.TransientModel):
	_name = 'lang.wizz'

	# potFile = fields.Binary(string='pot file')

	def get_pot(self):
		# self.ensure_one()
		base_url = self.env['ir.config_parameter'].get_param('web.base.url')
		print(potsrc)
		# print(str(glob.glob(home+"/**/*.pot").pop(0)))
		with open(potsrc, 'w', encoding="utf-8") as f:
			for file in filenames:
				with open(file, encoding="utf-8") as infile:
					f.write(str(infile.read()) + '\n')
		# for rec in self:
		# 	rec.state = 'ready'

# code snipet for downloading file
	def dl_pot(self):
		self.ensure_one()
		# for rec in self:
		# 	rec.state = 'done'
		return {
			'type': 'ir.actions.act_url',
			'url': potsrc+str('?download=true'),
			'target': 'self',
		}
