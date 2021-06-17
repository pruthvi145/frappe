# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CommunicationLink(Document):
	pass

def on_doctype_update():
	frappe.db.add_index("Communication Link", ["link_doctype", "link_name"])