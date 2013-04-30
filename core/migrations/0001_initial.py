# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AppUser'
        db.create_table(u'core_appuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('fb_user_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('fb_access_token', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'core', ['AppUser'])

        # Adding model 'Sport'
        db.create_table(u'core_sport', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('sports_data_id', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Sport'])

        # Adding model 'League'
        db.create_table(u'core_league', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('sport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Sport'])),
            ('sports_data_id', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('in_season', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'core', ['League'])

        # Adding model 'Conference'
        db.create_table(u'core_conference', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('sports_data_id', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True)),
            ('league', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.League'])),
        ))
        db.send_create_signal(u'core', ['Conference'])

        # Adding model 'Division'
        db.create_table(u'core_division', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, primary_key=True)),
            ('sports_data_id', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True)),
            ('conference', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Conference'])),
            ('league', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.League'])),
        ))
        db.send_create_signal(u'core', ['Division'])

        # Adding model 'Team'
        db.create_table(u'core_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sports_data_id', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, db_index=True, blank=True)),
            ('league', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.League'])),
            ('sport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Sport'])),
            ('conference', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Conference'], null=True, blank=True)),
            ('division', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Division'], null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Team'])

        # Adding model 'Game'
        db.create_table(u'core_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('home', self.gf('django.db.models.fields.related.ForeignKey')(related_name='game_set_home', to=orm['core.Team'])),
            ('away', self.gf('django.db.models.fields.related.ForeignKey')(related_name='game_set_away', to=orm['core.Team'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
            ('sports_data_id', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('league', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.League'])),
            ('gamestatus', self.gf('django.db.models.fields.IntegerField')(default=None, max_length=20, db_index=True)),
            ('last_updated_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Game'])


    def backwards(self, orm):
        # Deleting model 'AppUser'
        db.delete_table(u'core_appuser')

        # Deleting model 'Sport'
        db.delete_table(u'core_sport')

        # Deleting model 'League'
        db.delete_table(u'core_league')

        # Deleting model 'Conference'
        db.delete_table(u'core_conference')

        # Deleting model 'Division'
        db.delete_table(u'core_division')

        # Deleting model 'Team'
        db.delete_table(u'core_team')

        # Deleting model 'Game'
        db.delete_table(u'core_game')


    models = {
        u'core.appuser': {
            'Meta': {'object_name': 'AppUser'},
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'fb_access_token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fb_user_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'core.conference': {
            'Meta': {'object_name': 'Conference'},
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.League']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'sports_data_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'core.division': {
            'Meta': {'object_name': 'Division'},
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Conference']"}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.League']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'}),
            'sports_data_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'core.game': {
            'Meta': {'object_name': 'Game'},
            'away': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_set_away'", 'to': u"orm['core.Team']"}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'gamestatus': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'max_length': '20', 'db_index': 'True'}),
            'home': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_set_home'", 'to': u"orm['core.Team']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.League']"}),
            'sports_data_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'core.league': {
            'Meta': {'object_name': 'League'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'in_season': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'sport': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Sport']"}),
            'sports_data_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'core.sport': {
            'Meta': {'object_name': 'Sport'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'sports_data_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'core.team': {
            'Meta': {'object_name': 'Team'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Conference']", 'null': 'True', 'blank': 'True'}),
            'division': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Division']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.League']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sport': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Sport']"}),
            'sports_data_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'db_index': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']