from django.core.management.base import BaseCommand
from django.utils import simplejson
from core.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        json = open('core/data/data.json').read()
        data = simplejson.loads(json)
        new_data = []

        # Let's trim this down to what we want...
        sport = {'fields': {}}
        for key, value in data['sport'].iteritems():
            if key in ['pk', 'model']:
                sport[key] = value
            elif key in ['name', 'sports_data_id']:
                sport['fields'][key] = value
        new_data.append(sport)

        league = {'fields': {}}
        for key, value in data['league'].iteritems():
            if key in ['pk', 'model']:
                league[key] = value
            elif key in ['name', 'sport', 'sports_data_id', 'active', 'in_season']:
                league['fields'][key] = value
        new_data.append(league)

        for conf in data['conferences']:
            conference = {'fields': {}}
            for key, value in conf.iteritems():
                if key in ['pk', 'model']:
                    conference[key] = value
                elif key in ['name', 'sports_data_id', 'league']:
                    conference['fields'][key] = value
            new_data.append(conference)

        for div in data['divisions']:
            division = {'fields': {}}
            for key, value in div.iteritems():
                if key in ['pk', 'model']:
                    division[key] = value
                elif key in ['name', 'sports_data_id', 'league', 'conference']:
                    division['fields'][key] = value
            new_data.append(division)

        for t in data['teams']:
            team = {'pk': None, 'fields': {}}
            for key, value in t.iteritems():
                if key in ['model']:
                    team[key] = value
                elif key in ['name', 'city', 'abbreviation', 'sports_data_id', 'league', 'sport', 'conference', 'division']:
                    team['fields'][key] = value
            new_data.append(team)

        with open('core/data/fixture_data.json', 'w') as out:
            out.write(simplejson.dumps(new_data, separators=(',', ':')))
