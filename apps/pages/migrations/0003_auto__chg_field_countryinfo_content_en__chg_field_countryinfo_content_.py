# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'CountryInfo.content_en'
        db.alter_column('pages_countryinfo', 'content_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CountryInfo.content_ru'
        db.alter_column('pages_countryinfo', 'content_ru', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CountryInfo.content'
        db.alter_column('pages_countryinfo', 'content', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CountryInfo.content_de'
        db.alter_column('pages_countryinfo', 'content_de', self.gf('django.db.models.fields.TextField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'CountryInfo.content_en'
        db.alter_column('pages_countryinfo', 'content_en', self.gf('django.db.models.fields.TextField')(default=''))

        # User chose to not deal with backwards NULL issues for 'CountryInfo.content_ru'
        raise RuntimeError("Cannot reverse this migration. 'CountryInfo.content_ru' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'CountryInfo.content'
        raise RuntimeError("Cannot reverse this migration. 'CountryInfo.content' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'CountryInfo.content_de'
        raise RuntimeError("Cannot reverse this migration. 'CountryInfo.content_de' and its values cannot be restored.")


    models = {
        'pages.countryinfo': {
            'Meta': {'object_name': 'CountryInfo'},
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'content_de': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'content_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'content_ru': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'pages.news': {
            'Meta': {'ordering': "['-created']", 'object_name': 'News'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_de': ('django.db.models.fields.TextField', [], {}),
            'content_en': ('django.db.models.fields.TextField', [], {}),
            'content_ru': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'title_de': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'pages.staticpage': {
            'Meta': {'object_name': 'StaticPage'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_de': ('django.db.models.fields.TextField', [], {}),
            'content_en': ('django.db.models.fields.TextField', [], {}),
            'content_ru': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'title_de': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'world.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['pages']
