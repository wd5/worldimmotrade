# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Country.name_ru'
        db.add_column('world_country', 'name_ru', self.gf('django.db.models.fields.CharField')(max_length=50), keep_default=False)

        # Adding field 'Country.name_en'
        db.add_column('world_country', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=50), keep_default=False)

        # Adding field 'Country.name_de'
        db.add_column('world_country', 'name_de', self.gf('django.db.models.fields.CharField')(max_length=50), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Country.name_ru'
        db.delete_column('world_country', 'name_ru')

        # Deleting field 'Country.name_en'
        db.delete_column('world_country', 'name_en')

        # Deleting field 'Country.name_de'
        db.delete_column('world_country', 'name_de')


    models = {
        'world.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Region']"})
        },
        'world.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'world.region': {
            'Meta': {'ordering': "['name']", 'object_name': 'Region'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['world']
