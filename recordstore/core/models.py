from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from collect.consumer import database_search_barcode, database_release


class Collection(models.Model):
    """
    Represents a collection
    """
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)

    def __str__(self):
        """
        Returns the name of this object
        """
        return self.name


class Artist(models.Model):
    """
    Represents an artist
    """
    collection = models.ForeignKey(Collection)
    name = models.CharField(max_length=200)

    def __str__(self):
        """
        Returns the name of this object
        """
        return '{} - {}'.format(self.collection.name, self.name)


class Track(models.Model):
    """
    Represents a track
    """
    artist = models.ForeignKey(Artist)
    collection = models.ForeignKey(Collection)
    name = models.CharField(max_length=200)

    def __str__(self):
        """
        Returns the name of this object
        """
        return '{} - {} - {}'.format(self.collection.name, self.artist.name, self.name)


class Release(models.Model):
    """
    Represents an album
    """
    artist = models.ForeignKey(Artist, blank=True, null=True)
    barcode = models.CharField(blank=True, null=True, max_length=13)
    collection = models.ForeignKey(Collection)
    name = models.CharField(max_length=200)
    track = models.ManyToManyField(Track, blank=True)

    def collect_info(self):
        """
        Collects and stores information about release
        """
        info = database_search_barcode(self.barcode)
        results = info['results']
        if results:
            self._process_result(results[0])

    def _process_result(self, result):
        """
        Processes the results for release
        """
        dc_release = database_release(result['id'])
        artist = self._process_artist(dc_release)

        if artist:
            self._process_release(artist, dc_release)
            self._process_tracks(artist, dc_release)

    def _process_release(self, artist, dc_release):
        """
        Stores the name of the release based on result
        """
        self.artist = artist
        self.name = dc_release['title']
        self.save()

    def _process_artist(self, dc_release):
        """
        Finds or creates artist based on result
        """
        artists = dc_release['artists']

        if artists:
            artist_name = artists[0]['name']

            if Artist.objects.filter(collection=self.collection, name=artist_name):
                artist = Artist.objects.filter(collection=self.collection, name=artist_name)[0]
            else:
                artist = Artist.objects.create(collection=self.collection, name=artist_name)

            return artist

    def _process_tracks(self, artist, dc_release):
        """
        Creates tracks for release if not existing
        """
        dc_tracklist = dc_release['tracklist']
        for track in dc_tracklist:
            if not Track.objects.filter(collection=self.collection, artist=artist, name=track['title']):
                self.track.create(collection=self.collection, artist=artist, name=track['title'])

    def __str__(self):
        """
        Returns the name of this object
        """
        return '{} - {} - {}'.format(self.collection.name, self.artist.name, self.name)
