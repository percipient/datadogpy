from datadog.util.compat import urlparse
from datadog.api.base import CreateableAPIResource, ActionAPIResource, GetableAPIResource, ListableAPIResource


class Graph(CreateableAPIResource, ActionAPIResource):
    """
    A wrapper around Graph HTTP API.
    """
    _class_url = '/graph/snapshot'

    @classmethod
    def create(cls, **params):
        """
        Take a snapshot of a graph, returning the full url to the snapshot.

        :param metric_query: metric query
        :type metric_query: string query

        :param start: query start timestamp
        :type start: POSIX timestamp

        :param end: query end timestamp
        :type end: POSIX timestamp

        :param event_query: a query that will add event bands to the graph
        :type event_query: string query

        :returns: JSON response from HTTP API request
        """
        return super(Graph, cls).create(method='GET', **params)

    @classmethod
    def status(cls, snapshot_url):
        """
        Returns the status code of snapshot. Can be used to know when the
        snapshot is ready for download.

        :param snapshot_url: snapshot URL to check
        :type snapshot_url: string url

        :returns: JSON response from HTTP API request
        """
        snap_path = urlparse(snapshot_url).path
        snap_path = snap_path.split('/snapshot/view/')[1].split('.png')[0]
        snapshot_status_url = '/graph/snapshot_status/{0}'.format(snap_path)

        return super(Graph, cls)._trigger_action('GET', snapshot_status_url)


class Embed(ListableAPIResource, GetableAPIResource, ActionAPIResource):
    """
    A wrapper around Embed HTTP API.
    """
    _class_url = '/graph/embed'

    @classmethod
    def get_all(cls):
        """
        Returns a JSON object containing a list of all embeddable graphs
        in the API user's organization.

        :returns: JSON response from HTTP API request
        """
        return super(Embed, cls).get_all()

    @classmethod
    def get(cls, embed_id, **params):
        """
        Returns a JSON object representing the specified embed.

        :param embed_id:
        :type embed_id:

        :returns: JSON response from HTTP API request
        """
        return super(Embed, cls).get(embed_id, **params)

    @classmethod
    def create(cls, **params):
        """
        Returns a JSON object representing the specified embed.

        :param graph_json:
        :type graph_json:

        :param timeframe:
        :type timeframe:

        :param size:
        :type size:

        :param legend:
        :type legend:

        :param template_vars:
        :type template_vars:

        :returns: JSON response from HTTP API request
        """
        return super(Graph, cls)._trigger_action('POST', name=cls._class_url, **params)

    @classmethod
    def enable(cls, embed_id, **params):
        """
        Enable a specified embed.

        :param embed_id:
        :type embed_id:

        :returns: JSON response from HTTP API request
        """
        handle = embed_id + "/enable"
        return super(Embed, cls).get(handle)

    @classmethod
    def revoke(cls, embed_id):
        """
        Revoke a specified embed.

        :param embed_id:
        :type embed_id:

        :returns: JSON response from HTTP API request
        """
        handle = embed_id + "/revoke"
        return super(Embed, cls).get(handle)
