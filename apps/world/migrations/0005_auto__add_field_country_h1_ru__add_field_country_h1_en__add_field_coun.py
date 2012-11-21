# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Country.h1_ru'
        db.add_column('world_country', 'h1_ru', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Country.h1_en'
        db.add_column('world_country', 'h1_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Country.h1_de'
        db.add_column('world_country', 'h1_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Country.h1_ru'
        db.delete_column('world_country', 'h1_ru')

        # Deleting field 'Country.h1_en'
        db.delete_column('world_country', 'h1_en')

        # Deleting field 'Country.h1_de'
        db.delete_column('world_country', 'h1_de')


    models = {
        'world.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Region']"})
        },
        'world.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'h1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'h1_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'h1_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'h1_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'world.region': {
            'Meta': {'ordering': "['name']", 'object_name': 'Region'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['world']