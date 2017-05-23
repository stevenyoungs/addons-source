register(QUICKREPORT,
         id = 'Descendant Count Quickview',
         name = _("Descendant Count"),
         category = CATEGORY_QR_MISC,
         runfunc = "run",
         status = STABLE,
         description= _("Display descendant counts for each person."),
         fname="DescendantCount.py",
         authors=["Douglas S. Blank"],
         authors_email=["doug.blank@gmail.com"],
         version = '1.0.24',
         gramps_target_version = "5.1",
         )

register(GRAMPLET,
         id="Descendant Count Gramplet",
         name=_("Descendant Count Gramplet"),
         description = _("Gramplet for showing people and descendant counts"),
         status= STABLE,
         fname="DescendantCount.py",
         height=300,
         expand=True,
         gramplet = "DescendantCountGramplet",
         gramplet_title=_("Descendant Count"),
         detached_width = 600,
         detached_height = 400,
         version = '1.0.25',
         gramps_target_version = "5.1",
         help_url="Descendant_Count_Gramplet",
         )

