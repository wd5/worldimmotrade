# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'EstateTypeSeoText.country'
        db.add_column('estates_estatetypeseotext', 'country', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['world.Country']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'EstateTypeSeoText.country'
        db.delete_column('estates_estatetypeseotext', 'country_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'estates.additionalequipmentchoices': {
            'Meta': {'object_name': 'AdditionalEquipmentChoices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.apartament': {
            'Meta': {'object_name': 'Apartament'},
            'additional_costs': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'additional_equipment': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.AdditionalEquipmentChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'aviable_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'aviable_now': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'aviable_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'bathroom': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.BathroomChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'bathrooms_count': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'bedrooms_count': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'built_year': ('django.db.models.fields.IntegerField', [], {'default': "''", 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.City']"}),
            'client_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'comfort': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.ComfortChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'commission': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'condition': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.ConditionChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Country']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dist_to_airport': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dist_to_beach': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dist_to_centre': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dist_to_highway': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dist_to_kindergarten': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dist_to_park': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dist_to_recreation': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dist_to_school': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dist_to_sea': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dist_to_shopping': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dist_to_slopes': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dist_to_sports': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dist_to_station': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dist_to_transport': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dist_to_university': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'estate_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'floor': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'floor_covering': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.FloorCoveringOptions']", 'symmetrical': 'False', 'blank': 'True'}),
            'floor_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.FloorTypeChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'floors_count': ('django.db.models.fields.IntegerField', [], {'default': "''", 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'for_students': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'furnishings': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.FurnishingChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'glass_frame': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.GlassFrameChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'glazing': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.GlazingChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'heating': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.HeatingOptions']", 'symmetrical': 'False', 'blank': 'True'}),
            'historical_monument': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'kitchen_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.KitchenChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'kitchens_count': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'land_space': ('django.db.models.fields.IntegerField', [], {'default': "''", 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'living_space': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'location': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.LocationChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_location_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_location_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_location_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'only_for_students': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other_facilies': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.OtherFacilitieChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'parking_count': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'possible_bargain': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'possible_redevelopment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prepayment': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': "''"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Region']"}),
            'rent_for': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.RentForChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'rooms_count': ('django.db.models.fields.IntegerField', [], {'default': "''"}),
            'security_systems': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.SecuritySystemsChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'separate_toilets_count': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'show_on_start_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'students': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'total_space': ('django.db.models.fields.IntegerField', [], {'default': "''", 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '5'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'window_view': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.WindowViewChoices']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'estates.bathroomchoices': {
            'Meta': {'object_name': 'BathroomChoices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.bookmarks': {
            'Meta': {'object_name': 'Bookmarks'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estates.Apartament']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'estates.comfortchoices': {
            'Meta': {'object_name': 'ComfortChoices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.conditionchoices': {
            'Meta': {'object_name': 'ConditionChoices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.document': {
            'Meta': {'object_name': 'Document'},
            'apartament': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estates.Apartament']"}),
            'file_name': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'estates.estatetypeseotext': {
            'Meta': {'object_name': 'EstateTypeSeoText'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': "orm['world.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_id': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'estates.floorcoveringoptions': {
            'Meta': {'object_name': 'FloorCoveringOptions'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.floortypechoices': {
            'Meta': {'object_name': 'FloorTypeChoices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.furnishingchoices': {
            'Meta': {'object_name': 'FurnishingChoices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.glassframechoices': {
            'Meta': {'object_name': 'GlassFrameChoices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.glazingchoices': {
            'Meta': {'object_name': 'GlazingChoices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.heatingoptions': {
            'Meta': {'object_name': 'HeatingOptions'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.kitchenchoices': {
            'Meta': {'object_name': 'KitchenChoices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.locationchoices': {
            'Meta': {'object_name': 'LocationChoices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.otherfacilitiechoices': {
            'Meta': {'object_name': 'OtherFacilitieChoices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.photo': {
            'Meta': {'object_name': 'Photo'},
            'apartament': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estates.Apartament']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'estates.rentforchoices': {
            'Meta': {'object_name': 'RentForChoices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.securitysystemschoices': {
            'Meta': {'object_name': 'SecuritySystemsChoices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'estates.windowviewchoices': {
            'Meta': {'object_name': 'WindowViewChoices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
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
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'otmenok': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'seo_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'world.region': {
            'Meta': {'ordering': "['name']", 'object_name': 'Region'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['estates']
