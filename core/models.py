from django.db import models, IntegrityError
from django.contrib.auth.models import AbstractBaseUser

from core.managers import AppUserManager
from django_serialize.models import SerializeMixin

import ast

class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class AppUser(AbstractBaseUser, SerializeMixin):
    # required
    email = models.CharField(max_length=255, unique=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)
    full_name = models.CharField(max_length=140)

    # fb
    fb_user_id = models.CharField(max_length=20)
    fb_access_token = models.CharField(max_length=255, null=True) # FIXME: access_tokens can now be > 255 chars ?

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name'] # only relevant to ./manage.py createsuperuser

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __unicode__(self):
        return self.email

    def serialize_options(self, version=None):
        return {
            'excludes': ('password', 'is_admin')
        }

class Sport(models.Model, SerializeMixin):
    name = models.CharField(primary_key=True, max_length=50)
    sports_data_id = models.CharField(max_length=100, blank=True, null=True, default=None)

    #last_updated_time = models.DateTimeField(auto_now=True, db_index=True)
    #created_time = models.DateTimeField(auto_now_add=True)

class League(models.Model, SerializeMixin):
    name = models.CharField(primary_key=True, max_length=20) #always lowercase
    sport = models.ForeignKey(Sport, db_index=True)
    sports_data_id = models.CharField(max_length=100, blank=True, null=True, default=None)
    
    active = models.BooleanField(default=True)
    in_season = models.BooleanField(default=False)

    #last_updated_time = models.DateTimeField(auto_now=True, db_index=True)
    #created_time = models.DateTimeField(auto_now_add=True)

class Conference(models.Model, SerializeMixin):
    name = models.CharField(primary_key=True, max_length=20)
    sports_data_id = models.CharField(max_length=100, blank=True, null=True, default=None)
    league = models.ForeignKey(League)

    #last_updated_time = models.DateTimeField(auto_now=True)
    #created_time = models.DateTimeField(auto_now_add=True)

class Division(models.Model, SerializeMixin):
    name = models.CharField(primary_key=True, max_length=40)
    sports_data_id = models.CharField(max_length=100, blank=True, null=True, default=None)
    conference = models.ForeignKey(Conference)
    league = models.ForeignKey(League)

    #last_updated_time = models.DateTimeField(auto_now=True)
    #created_time = models.DateTimeField(auto_now_add=True)

class Team(models.Model, SerializeMixin):
    name = models.CharField(max_length=100) # for example: Boilermakers
    city = models.CharField(max_length=50) # for example: Purdue
    abbreviation = models.CharField(max_length=10)
    sports_data_id = models.CharField(max_length=100, blank=True, null=True, default=None, db_index=True)

    league = models.ForeignKey(League, db_index=True)
    sport = models.ForeignKey(Sport, db_index=True)
    conference = models.ForeignKey(Conference, blank=True, null=True, default=None)
    division = models.ForeignKey(Division, blank=True, null=True, default=None)
        
    #last_updated_time = models.DateTimeField(auto_now=True, db_index=True)
    #created_time = models.DateTimeField(auto_now_add=True)

class Game(models.Model, SerializeMixin):
    PRE_GAME = 1
    IN_PROGRESS = 2
    FINAL = 3
    CANCELLED = 4
    GAME_STATUS = (
        (PRE_GAME, 'Pre-Game'),
        (IN_PROGRESS, 'In-Progress'),
        (FINAL, 'Final'),
        (CANCELLED, 'Cancelled'),
    )

    home = models.ForeignKey(Team, related_name='game_set_home')
    away = models.ForeignKey(Team, related_name='game_set_away')

    start_time = models.DateTimeField(blank=True, null=True, default=None)
    end_time = models.DateTimeField(blank=True, null=True, default=None)
    sports_data_id = models.CharField(max_length=50, blank=True, null=True, default=None)
    league = models.ForeignKey(League, db_index=True)
    gamestatus = models.IntegerField(max_length=20, choices=GAME_STATUS, default=None, db_index=True)

    
    def serialize_options(self, version=None):
        return {
            'relations': ('home', 'away')
        }
    

class Match(models.Model, SerializeMixin):
    code = models.IntegerField(null=True, unique=True)
    active = models.BooleanField(default=True)

    player = models.ForeignKey(AppUser, related_name='match_set_player')
    opponent = models.ForeignKey(AppUser, related_name='match_set_opponent', null=True)

    '''
    @property
    def player_picks(self):
        if not self._player_picks:
            self._player_picks = Team.objects.filter(pk=self.player_picks_ids)
        return self._player_picks

    @player_picks.setter
    def player_picks(self, teams):
        self.player_picks_ids = [t.pk for t in teams]
        if self._player_picks:
            self._player_picks = teams

    @property
    def opponent_picks(self):
        if not self._opponent_picks:
            self._opponent_picks = Team.objects.filter(pk=self.opponent_picks_ids)
        return self._opponent_picks

    @opponent_picks.setter
    def opponent_picks(self, teams):
        self.opponent_picks_ids = [t.pk for t in teams]
        if self._opponent_picks:
            self._opponent_picks = teams
    '''

    def __init__(self, *args, **kwargs):
        super(Match, self).__init__(*args, **kwargs)
        if not self.code:
            self.code = self.get_match_code()

    '''
    def save(self, *args, **kwargs):
        # Code might be taken, by default we'll re-save with a new code.
        # FIXME: Codes are going to fill up eventually. Have an active state and then do unique together
        # Active and code
        try:
            super(Match, self).save(*args, **kwargs)
        except IntegrityError:
            self.code = self.get_match_code()
            super(Match, self).save(*args, **kwargs)
    '''

    def get_match_code(self):
        from random import randint
        a_prime = 3571
        num = 4120
        return (randint(0, 3571) * num) % a_prime

class Pick(models.Model, SerializeMixin):
    match = models.ForeignKey(Match)
    player = models.ForeignKey(AppUser)
    team = models.ForeignKey(Team)
    game = models.ForeignKey(Game)
