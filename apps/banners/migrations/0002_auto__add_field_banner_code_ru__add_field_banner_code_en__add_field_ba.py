# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Banner.code_ru'
        db.add_column('banners_banner', 'code_ru', self.gf('django.db.models.fields.TextField')(), keep_default=False)

        # Adding field 'Banner.code_en'
        db.add_column('banners_banner', 'code_en', self.gf('django.db.models.fields.TextField')(), keep_default=False)

        # Adding field 'Banner.code_de'
        db.add_column('banners_banner', 'code_de', self.gf('django.db.models.fields.TextField')(), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Banner.code_ru'
        db.delete_column('banners_banner', 'code_ru')

        # Deleting field 'Banner.code_en'
        db.delete_column('banners_banner', 'code_en')

        # Deleting field 'Banner.code_de'
        db.delete_column('banners_banner', 'code_de')


    models = {
        'banners.banner': {
            'Meta': {'object_name': 'Banner'},
            'code': ('django.db.models.fields.TextField', [], {}),
            'code_de': ('django.db.models.fields.TextField', [], {}),
            'code_en': ('django.db.models.fields.TextField', [], {}),
            'code_ru': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['banners']
