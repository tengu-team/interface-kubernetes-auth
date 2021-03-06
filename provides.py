#!/usr/bin/env python3
# Copyright (C) 2016  Ghent University
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class KubernetesAuthProvides(RelationBase):
    scope = scopes.GLOBAL

    @hook('{provides:kubernetes-auth}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.available')

    @hook('{provides:kubernetes-auth}-relation-{departed}')
    def broken(self):
        self.remove_state('{relation_name}.available')

    def send_config(self, config):
        """Sends the kube config file via dict
        """
        self.set_remote('kube_config', config)
