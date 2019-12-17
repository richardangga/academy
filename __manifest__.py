{
	"name"			:"Addon Academy Odoo",
	"version"		:"1.0",
	"depends"		:["base","account"],
	"author"		:"richard",
	"category"		:"Education",
	"website"		:"htpp://vitraining.com",
	"Description"	:"...",
	"data"			:[
	 "menu.xml",
	 "security/ir.model.access.csv",
	 "course.xml",
	 "session.xml",
	 "attendee.xml",
	 "partner.xml",
	 "security/group.xml",
	 "wizard/create_attendee_view.xml",
	 "report/session.xml"
	],
	"installable": True,
	"auto_install": False,
	"application": True,
}