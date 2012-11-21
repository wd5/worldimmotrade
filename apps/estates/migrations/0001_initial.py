# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'KitchenChoices'
        db.create_table('estates_kitchenchoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['KitchenChoices'])

        # Adding model 'ComfortChoices'
        db.create_table('estates_comfortchoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['ComfortChoices'])

        # Adding model 'RentForChoices'
        db.create_table('estates_rentforchoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['RentForChoices'])

        # Adding model 'LocationChoices'
        db.create_table('estates_locationchoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['LocationChoices'])

        # Adding model 'FloorTypeChoices'
        db.create_table('estates_floortypechoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['FloorTypeChoices'])

        # Adding model 'HeatingOptions'
        db.create_table('estates_heatingoptions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['HeatingOptions'])

        # Adding model 'FloorCoveringOptions'
        db.create_table('estates_floorcoveringoptions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['FloorCoveringOptions'])

        # Adding model 'BathroomChoices'
        db.create_table('estates_bathroomchoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['BathroomChoices'])

        # Adding model 'OtherFacilitieChoices'
        db.create_table('estates_otherfacilitiechoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['OtherFacilitieChoices'])

        # Adding model 'SecuritySystemsChoices'
        db.create_table('estates_securitysystemschoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['SecuritySystemsChoices'])

        # Adding model 'FurnishingChoices'
        db.create_table('estates_furnishingchoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['FurnishingChoices'])

        # Adding model 'AdditionalEquipmentChoices'
        db.create_table('estates_additionalequipmentchoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['AdditionalEquipmentChoices'])

        # Adding model 'GlazingChoices'
        db.create_table('estates_glazingchoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['GlazingChoices'])

        # Adding model 'GlassFrameChoices'
        db.create_table('estates_glassframechoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['GlassFrameChoices'])

        # Adding model 'WindowViewChoices'
        db.create_table('estates_windowviewchoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['WindowViewChoices'])

        # Adding model 'ConditionChoices'
        db.create_table('estates_conditionchoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('estates', ['ConditionChoices'])

        # Adding model 'Apartament'
        db.create_table('estates_apartament', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('type', self.gf('django.db.models.fields.CharField')(default=0, max_length=5)),
            ('for_students', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('only_for_students', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['world.Country'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['world.Region'])),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['world.City'])),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('price_for_m2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('commission', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('additional_costs', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('prepayment', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('possible_bargain', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('estate_type', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('aviable_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('aviable_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('aviable_now', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('built_year', self.gf('django.db.models.fields.IntegerField')(default='', max_length=4, null=True, blank=True)),
            ('living_space', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('living_space_for_m2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('total_space', self.gf('django.db.models.fields.IntegerField')(default='', max_length=4, null=True, blank=True)),
            ('total_space_for_m2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('land_space', self.gf('django.db.models.fields.IntegerField')(default='', max_length=4, null=True, blank=True)),
            ('land_space_for_m2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rooms_count', self.gf('django.db.models.fields.IntegerField')(default='')),
            ('bedrooms_count', self.gf('django.db.models.fields.IntegerField')(default='', null=True, blank=True)),
            ('floor', self.gf('django.db.models.fields.IntegerField')(default='', null=True, blank=True)),
            ('floors_count', self.gf('django.db.models.fields.IntegerField')(default='', max_length=5, null=True, blank=True)),
            ('kitchens_count', self.gf('django.db.models.fields.IntegerField')(default='', null=True, blank=True)),
            ('bathrooms_count', self.gf('django.db.models.fields.IntegerField')(default='', null=True, blank=True)),
            ('separate_toilets_count', self.gf('django.db.models.fields.IntegerField')(default='', null=True, blank=True)),
            ('parking_count', self.gf('django.db.models.fields.IntegerField')(default='', null=True, blank=True)),
            ('dist_to_station', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('dist_to_transport', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('dist_to_airport', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('dist_to_highway', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('dist_to_centre', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('dist_to_kindergarten', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('dist_to_school', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('dist_to_university', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('dist_to_shopping', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('dist_to_sea', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('dist_to_beach', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('dist_to_recreation', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('dist_to_park', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('dist_to_slopes', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('dist_to_sports', self.gf('django.db.models.fields.FloatField')(default='', null=True, blank=True)),
            ('historical_monument', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('possible_redevelopment', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description_ru', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description_de', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('object_location', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('object_location_ru', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('object_location_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('object_location_de', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('estates', ['Apartament'])

        # Adding M2M table for field rent_for on 'Apartament'
        db.create_table('estates_apartament_rent_for', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('rentforchoices', models.ForeignKey(orm['estates.rentforchoices'], null=False))
        ))
        db.create_unique('estates_apartament_rent_for', ['apartament_id', 'rentforchoices_id'])

        # Adding M2M table for field location on 'Apartament'
        db.create_table('estates_apartament_location', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('locationchoices', models.ForeignKey(orm['estates.locationchoices'], null=False))
        ))
        db.create_unique('estates_apartament_location', ['apartament_id', 'locationchoices_id'])

        # Adding M2M table for field floor_type on 'Apartament'
        db.create_table('estates_apartament_floor_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('floortypechoices', models.ForeignKey(orm['estates.floortypechoices'], null=False))
        ))
        db.create_unique('estates_apartament_floor_type', ['apartament_id', 'floortypechoices_id'])

        # Adding M2M table for field heating on 'Apartament'
        db.create_table('estates_apartament_heating', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('heatingoptions', models.ForeignKey(orm['estates.heatingoptions'], null=False))
        ))
        db.create_unique('estates_apartament_heating', ['apartament_id', 'heatingoptions_id'])

        # Adding M2M table for field floor_covering on 'Apartament'
        db.create_table('estates_apartament_floor_covering', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('floorcoveringoptions', models.ForeignKey(orm['estates.floorcoveringoptions'], null=False))
        ))
        db.create_unique('estates_apartament_floor_covering', ['apartament_id', 'floorcoveringoptions_id'])

        # Adding M2M table for field kitchen_type on 'Apartament'
        db.create_table('estates_apartament_kitchen_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('kitchenchoices', models.ForeignKey(orm['estates.kitchenchoices'], null=False))
        ))
        db.create_unique('estates_apartament_kitchen_type', ['apartament_id', 'kitchenchoices_id'])

        # Adding M2M table for field bathroom on 'Apartament'
        db.create_table('estates_apartament_bathroom', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('bathroomchoices', models.ForeignKey(orm['estates.bathroomchoices'], null=False))
        ))
        db.create_unique('estates_apartament_bathroom', ['apartament_id', 'bathroomchoices_id'])

        # Adding M2M table for field other_facilies on 'Apartament'
        db.create_table('estates_apartament_other_facilies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('otherfacilitiechoices', models.ForeignKey(orm['estates.otherfacilitiechoices'], null=False))
        ))
        db.create_unique('estates_apartament_other_facilies', ['apartament_id', 'otherfacilitiechoices_id'])

        # Adding M2M table for field security_systems on 'Apartament'
        db.create_table('estates_apartament_security_systems', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('securitysystemschoices', models.ForeignKey(orm['estates.securitysystemschoices'], null=False))
        ))
        db.create_unique('estates_apartament_security_systems', ['apartament_id', 'securitysystemschoices_id'])

        # Adding M2M table for field comfort on 'Apartament'
        db.create_table('estates_apartament_comfort', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('comfortchoices', models.ForeignKey(orm['estates.comfortchoices'], null=False))
        ))
        db.create_unique('estates_apartament_comfort', ['apartament_id', 'comfortchoices_id'])

        # Adding M2M table for field furnishings on 'Apartament'
        db.create_table('estates_apartament_furnishings', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('furnishingchoices', models.ForeignKey(orm['estates.furnishingchoices'], null=False))
        ))
        db.create_unique('estates_apartament_furnishings', ['apartament_id', 'furnishingchoices_id'])

        # Adding M2M table for field additional_equipment on 'Apartament'
        db.create_table('estates_apartament_additional_equipment', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('additionalequipmentchoices', models.ForeignKey(orm['estates.additionalequipmentchoices'], null=False))
        ))
        db.create_unique('estates_apartament_additional_equipment', ['apartament_id', 'additionalequipmentchoices_id'])

        # Adding M2M table for field glazing on 'Apartament'
        db.create_table('estates_apartament_glazing', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('glazingchoices', models.ForeignKey(orm['estates.glazingchoices'], null=False))
        ))
        db.create_unique('estates_apartament_glazing', ['apartament_id', 'glazingchoices_id'])

        # Adding M2M table for field glass_frame on 'Apartament'
        db.create_table('estates_apartament_glass_frame', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('glassframechoices', models.ForeignKey(orm['estates.glassframechoices'], null=False))
        ))
        db.create_unique('estates_apartament_glass_frame', ['apartament_id', 'glassframechoices_id'])

        # Adding M2M table for field window_view on 'Apartament'
        db.create_table('estates_apartament_window_view', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('windowviewchoices', models.ForeignKey(orm['estates.windowviewchoices'], null=False))
        ))
        db.create_unique('estates_apartament_window_view', ['apartament_id', 'windowviewchoices_id'])

        # Adding M2M table for field condition on 'Apartament'
        db.create_table('estates_apartament_condition', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartament', models.ForeignKey(orm['estates.apartament'], null=False)),
            ('conditionchoices', models.ForeignKey(orm['estates.conditionchoices'], null=False))
        ))
        db.create_unique('estates_apartament_condition', ['apartament_id', 'conditionchoices_id'])

        # Adding model 'Bookmarks'
        db.create_table('estates_bookmarks', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estates.Apartament'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('estates', ['Bookmarks'])

        # Adding model 'Photo'
        db.create_table('estates_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apartament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estates.Apartament'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('estates', ['Photo'])


    def backwards(self, orm):
        
        # Deleting model 'KitchenChoices'
        db.delete_table('estates_kitchenchoices')

        # Deleting model 'ComfortChoices'
        db.delete_table('estates_comfortchoices')

        # Deleting model 'RentForChoices'
        db.delete_table('estates_rentforchoices')

        # Deleting model 'LocationChoices'
        db.delete_table('estates_locationchoices')

        # Deleting model 'FloorTypeChoices'
        db.delete_table('estates_floortypechoices')

        # Deleting model 'HeatingOptions'
        db.delete_table('estates_heatingoptions')

        # Deleting model 'FloorCoveringOptions'
        db.delete_table('estates_floorcoveringoptions')

        # Deleting model 'BathroomChoices'
        db.delete_table('estates_bathroomchoices')

        # Deleting model 'OtherFacilitieChoices'
        db.delete_table('estates_otherfacilitiechoices')

        # Deleting model 'SecuritySystemsChoices'
        db.delete_table('estates_securitysystemschoices')

        # Deleting model 'FurnishingChoices'
        db.delete_table('estates_furnishingchoices')

        # Deleting model 'AdditionalEquipmentChoices'
        db.delete_table('estates_additionalequipmentchoices')

        # Deleting model 'GlazingChoices'
        db.delete_table('estates_glazingchoices')

        # Deleting model 'GlassFrameChoices'
        db.delete_table('estates_glassframechoices')

        # Deleting model 'WindowViewChoices'
        db.delete_table('estates_windowviewchoices')

        # Deleting model 'ConditionChoices'
        db.delete_table('estates_conditionchoices')

        # Deleting model 'Apartament'
        db.delete_table('estates_apartament')

        # Removing M2M table for field rent_for on 'Apartament'
        db.delete_table('estates_apartament_rent_for')

        # Removing M2M table for field location on 'Apartament'
        db.delete_table('estates_apartament_location')

        # Removing M2M table for field floor_type on 'Apartament'
        db.delete_table('estates_apartament_floor_type')

        # Removing M2M table for field heating on 'Apartament'
        db.delete_table('estates_apartament_heating')

        # Removing M2M table for field floor_covering on 'Apartament'
        db.delete_table('estates_apartament_floor_covering')

        # Removing M2M table for field kitchen_type on 'Apartament'
        db.delete_table('estates_apartament_kitchen_type')

        # Removing M2M table for field bathroom on 'Apartament'
        db.delete_table('estates_apartament_bathroom')

        # Removing M2M table for field other_facilies on 'Apartament'
        db.delete_table('estates_apartament_other_facilies')

        # Removing M2M table for field security_systems on 'Apartament'
        db.delete_table('estates_apartament_security_systems')

        # Removing M2M table for field comfort on 'Apartament'
        db.delete_table('estates_apartament_comfort')

        # Removing M2M table for field furnishings on 'Apartament'
        db.delete_table('estates_apartament_furnishings')

        # Removing M2M table for field additional_equipment on 'Apartament'
        db.delete_table('estates_apartament_additional_equipment')

        # Removing M2M table for field glazing on 'Apartament'
        db.delete_table('estates_apartament_glazing')

        # Removing M2M table for field glass_frame on 'Apartament'
        db.delete_table('estates_apartament_glass_frame')

        # Removing M2M table for field window_view on 'Apartament'
        db.delete_table('estates_apartament_window_view')

        # Removing M2M table for field condition on 'Apartament'
        db.delete_table('estates_apartament_condition')

        # Deleting model 'Bookmarks'
        db.delete_table('estates_bookmarks')

        # Deleting model 'Photo'
        db.delete_table('estates_photo')


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
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
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
            'comfort': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.ComfortChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'commission': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'condition': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.ConditionChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Country']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_de': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'kitchen_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.KitchenChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'kitchens_count': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'land_space': ('django.db.models.fields.IntegerField', [], {'default': "''", 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'land_space_for_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'living_space': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'living_space_for_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.LocationChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'object_location': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'object_location_de': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'object_location_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'object_location_ru': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'only_for_students': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other_facilies': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.OtherFacilitieChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'parking_count': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'possible_bargain': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'possible_redevelopment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prepayment': ('django.db.models.fields.FloatField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'price_for_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Region']"}),
            'rent_for': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.RentForChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'rooms_count': ('django.db.models.fields.IntegerField', [], {'default': "''"}),
            'security_systems': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estates.SecuritySystemsChoices']", 'symmetrical': 'False', 'blank': 'True'}),
            'separate_toilets_count': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'total_space': ('django.db.models.fields.IntegerField', [], {'default': "''", 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'total_space_for_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '5'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Region']"})
        },
        'world.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'world.region': {
            'Meta': {'ordering': "['name']", 'object_name': 'Region'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['estates']
