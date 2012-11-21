# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'City.name'
        db.alter_column('world_city', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Adding index on 'City', fields ['name']
        db.create_index('world_city', ['name'])

        # Changing field 'Region.name'
        db.alter_column('world_region', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Country.name_ru'
        db.alter_column('world_country', 'name_ru', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Country.name_en'
        db.alter_column('world_country', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Country.name_de'
        db.alter_column('world_country', 'name_de', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Country.name'
        db.alter_column('world_country', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))


    def backwards(self, orm):
        
        # Removing index on 'City', fields ['name']
        db.delete_index('world_city', ['name'])

        # Changing field 'City.name'
        db.alter_column('world_city', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Region.name'
        db.alter_column('world_region', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # User chose to not deal with backwards NULL issues for 'Country.name_ru'
        raise RuntimeError("Cannot reverse this migration. 'Country.name_ru' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Country.name_en'
        raise RuntimeError("Cannot reverse this migration. 'Country.name_en' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Country.name_de'
        raise RuntimeError("Cannot reverse this migration. 'Country.name_de' and its values cannot be restored.")

        # Changing field 'Country.name'
        db.alter_column('world_country', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))


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
