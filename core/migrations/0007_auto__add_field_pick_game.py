# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pick.game'
        db.add_column(u'core_pick', 'game',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.Game']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Pick.game'
        db.delete_column(u'core_pick', 'game_id')


    models = {
        u'core.appuser': {
            'Meta': {'object_name': 'AppUser'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'fb_access_token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
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
            'end_time': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'gamestatus': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'max_length': '20', 'db_index': 'True'}),
            'home': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_set_home'", 'to': u"orm['core.Team']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        u'core.match': {
            'Meta': {'object_name': 'Match'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opponent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_set_opponent'", 'null': 'True', 'to': u"orm['core.AppUser']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_set_player'", 'to': u"orm['core.AppUser']"})
        },
        u'core.pick': {
            'Meta': {'object_name': 'Pick'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Match']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.AppUser']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Team']"})
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