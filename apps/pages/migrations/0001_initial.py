# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'StaticPage'
        db.create_table('pages_staticpage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('title_ru', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('title_de', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('url', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('content_ru', self.gf('django.db.models.fields.TextField')()),
            ('content_en', self.gf('django.db.models.fields.TextField')()),
            ('content_de', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('pages', ['StaticPage'])

        # Adding model 'News'
        db.create_table('pages_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('title_ru', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('title_de', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('content_ru', self.gf('django.db.models.fields.TextField')()),
            ('content_en', self.gf('django.db.models.fields.TextField')()),
            ('content_de', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('pages', ['News'])


    def backwards(self, orm):
        
        # Deleting model 'StaticPage'
        db.delete_table('pages_staticpage')

        # Deleting model 'News'
        db.delete_table('pages_news')


    models = {
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
        }
    }

    complete_apps = ['pages']
