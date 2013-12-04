# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field thirdpartycomponents on 'License'
        m2m_table_name = db.shorten_name(u'thirdparty_license_thirdpartycomponents')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('license', models.ForeignKey(orm[u'thirdparty.license'], null=False)),
            ('thirdpartycomponent', models.ForeignKey(orm[u'thirdparty.thirdpartycomponent'], null=False))
        ))
        db.create_unique(m2m_table_name, ['license_id', 'thirdpartycomponent_id'])


    def backwards(self, orm):
        # Removing M2M table for field thirdpartycomponents on 'License'
        db.delete_table(db.shorten_name(u'thirdparty_license_thirdpartycomponents'))


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
            'thirdpartycomponents': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['thirdparty.ThirdPartyComponent']", 'symmetrical': 'False'}),
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