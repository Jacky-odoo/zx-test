# -*- coding: utf-8 -*-

import os
import glob
import pandas as pd

from odoo import models, fields, api

home = os.path.expanduser("~")  # get root directory
filenames = glob.glob(home+"/**/*.pot")  # list of all .pot files in the root directory
potsrc = home+'/odoo/zx-test/zx-global-translate/i18n/zx-global-translate-generated.pot'  # .pot file location
# state = fields.Selection([
# 	('waiting', 'Waiting'),
# 	('ready', 'Ready'),
# 	('done', 'Done'),
# ], required=True, default='waiting')


class LangWizz(models.Model):
	_name = 'lang.wizz'

	someText = fields.Char(string='Some Text', required=True)
	potFile = fields.Binary(string='pot file')

	@api.multi
	def get_pot(self):
		self.ensure_one()
		print(home)
		with open(potsrc, 'w', encoding="utf-8") as f:
			for file in filenames:
				with open(file, encoding="utf-8") as infile:
					f.write(str(infile.read()) + '\n')
		# for rec in self:
		# 	rec.state = 'ready'

# code snipet for downloading file
	@api.multi
	def dl_pot(self):
		self.ensure_one()
		# for rec in self:
		# 	rec.state = 'done'
		return {
			'type': 'ir.actions.act_url',
			'url': potsrc,
			'target': 'self',
		}

	@api.multi
	def print_pandas(self):
		# place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
		df = pd.read_excel(r'C:\Users\Nejc\odoo\zx-test\zx-pot-wiz\tmp\pricelist-test.xlsx')
		print(df)
