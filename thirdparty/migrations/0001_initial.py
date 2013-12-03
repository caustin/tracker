# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'License'
        db.create_table(u'thirdparty_license', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('brief_description', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('acceptable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'thirdparty', ['License'])

        # Adding model 'ThirdPartyComponent'
        db.create_table(u'thirdparty_thirdpartycomponent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('license', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['thirdparty.License'])),
            ('download_link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('documentation_link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'thirdparty', ['ThirdPartyComponent'])


    def backwards(self, orm):
        # Deleting model 'License'
        db.delete_table(u'thirdparty_license')

        # Deleting model 'ThirdPartyComponent'
        db.delete_table(u'thirdparty_thirdpartycomponent')


    models = {
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
            'documentation_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'download_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['thirdparty.License']"}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['thirdparty']