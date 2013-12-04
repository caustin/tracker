# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ThirdPartyComponent.license'
        db.delete_column(u'thirdparty_thirdpartycomponent', 'license_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ThirdPartyComponent.license'
        raise RuntimeError("Cannot reverse this migration. 'ThirdPartyComponent.license' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ThirdPartyComponent.license'
        db.add_column(u'thirdparty_thirdpartycomponent', 'license',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['thirdparty.License']),
                      keep_default=False)


    models = {
        u'thirdparty.component': {
            'Meta': {'object_name': 'Component'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'thirdparty.license': {
            'Meta': {'object_name': 'License'},
            'acceptable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brief_description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'thirdparty.thirdpartycomponent': {
            'Meta': {'object_name': 'ThirdPartyComponent'},
            'component': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['thirdparty.Component']", 'null': 'True'}),
            'documentation_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'download_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['thirdparty']