from collections import OrderedDict

from synapse_tools.config_plugins.logging import Logging
from synapse_tools.config_plugins.path_based_routing import PathBasedRouting
from synapse_tools.config_plugins.proxied_through import ProxiedThrough

PLUGIN_REGISTRY = OrderedDict([
    ('proxied_through', ProxiedThrough),
    ('logging', Logging),
    ('path_based_routing', PathBasedRouting)
])
