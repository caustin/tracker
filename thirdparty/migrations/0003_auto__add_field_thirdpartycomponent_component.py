# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ThirdPartyComponent.component'
        db.add_column(u'thirdparty_thirdpartycomponent', 'component',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['thirdparty.Component'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ThirdPartyComponent.component'
        db.delete_column(u'thirdparty_thirdpartycomponent', 'component_id')


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
            'license': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['thirdparty.License']"}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['thirdparty']