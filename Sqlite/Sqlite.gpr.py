register(IMPORT,
         id    = 'im_sqlite',
         name  = _('SQLite Import'),
         description =  _('SQLite is a common local database format'),
         version = '1.0.35',
         gramps_target_version = "5.1",
         status = STABLE, # tested with python 3, need to review unicode usage
         include_in_listing = False,
         fname = 'ImportSql.py',
         import_function = 'importData',
         extension = "sql"
)

register(EXPORT,
         id    = 'ex_sqlite',
         name  = _('SQLite Export'),
         description =  _('SQLite is a common local database format'),
         version = '1.0.34',
         gramps_target_version = "5.1",
         status = STABLE, # tested with python 3 but still gives errors
         include_in_listing = False,
         fname = 'ExportSql.py',
         export_function = 'exportData',
         extension = "sql",
         export_options = 'WriterOptionBox'
)
