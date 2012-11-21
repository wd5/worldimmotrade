# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Banner.code'
        db.alter_column('banners_banner', 'code', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Banner.code_de'
        db.alter_column('banners_banner', 'code_de', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Banner.code_ru'
        db.alter_column('banners_banner', 'code_ru', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Banner.code_en'
        db.alter_column('banners_banner', 'code_en', self.gf('django.db.models.fields.TextField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'Banner.code'
        db.alter_column('banners_banner', 'code', self.gf('django.db.models.fields.TextField')(default='ok'))

        # Changing field 'Banner.code_de'
        db.alter_column('banners_banner', 'code_de', self.gf('django.db.models.fields.TextField')(default='ok'))

        # User chose to not deal with backwards NULL issues for 'Banner.code_ru'
        raise RuntimeError("Cannot reverse this migration. 'Banner.code_ru' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Banner.code_en'
        raise RuntimeError("Cannot reverse this migration. 'Banner.code_en' and its values cannot be restored.")


    models = {
        'banners.banner': {
            'Meta': {'object_name': 'Banner'},
            'code': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'code_de': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'code_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'code_ru': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['banners']
