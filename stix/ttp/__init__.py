# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.bindings.ttp as ttp_binding
from stix.common import StructuredText, VocabString, InformationSource
from .behavior import Behavior

class TTP(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.TTPType
    _namespace = "http://stix.mitre.org/TTP-1"
    _version = "1.1"

    def __init__(self, id_=None, title=None, description=None, short_description=None):
        self.id_ = id_ or stix.utils.create_id("ttp")
        self.version = self._version
        self.title = title
        self.description = description
        self.short_description = short_description
        self.behavior = None
        self.related_ttps = None
        self.information_source = None
        
        self.exploit_targets = None
        self.intended_effect = None
        self.resources = None
        self.victim_targeting = None
        
        
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value:
            if isinstance(value, StructuredText):
                self._description = value
            else:
                self._description = StructuredText(value=value)
        else:
            self._description = None

    @property
    def short_description(self):
        return self._short_description

    @short_description.setter
    def short_description(self, value):
        if value:
            if isinstance(value, StructuredText):
                self._short_description = value
            else:
                self._short_description = StructuredText(value=value)
        else:
            self._short_description = None

    @property
    def behavior(self):
        return self._behavior
    
    @behavior.setter
    def behavior(self, value):
        if not value:
            self._behavior = None
        elif isinstance(value, Behavior):
            self._behavior = value
        else:
            raise ValueError('Value must be a Behavior instance')

    @property
    def related_ttps(self):
        return self._related_ttps
    
    @related_ttps.setter
    def related_ttps(self, value):
        from .related_ttps import RelatedTTPs # avoid circular imports
        
        if not value:
            self._related_ttps = None
        elif isinstance(value, RelatedTTPs):
            self._related_ttps = value
        else:
            raise ValueError("value must be RelatedTTPs instance")

    @property
    def information_source(self):
        return self._information_source
    
    @information_source.setter
    def information_source(self, value):
        if not value:
            self._information_source = None
        elif isinstance(value, InformationSource):
            self._information_source = value
        else:
            raise ValueError('value must be instance of InformationSource')

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        return_obj.set_id(self.id_)
        return_obj.set_version(self.version)
        return_obj.set_Title(self.title)

        if self.description:
            return_obj.set_Description(self.description.to_obj())
        if self.short_description:
            return_obj.set_Short_Description(self.short_description.to_obj())
        if self.behavior:
            return_obj.set_Behavior(self.behavior.to_obj())
        if self.related_ttps:
            return_obj.set_Related_TTPs(self.related_ttps.to_obj())
        if self.information_source:
            return_obj.set_Information_Source(self.information_source.to_obj())
        
        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
        
        from .related_ttps import RelatedTTPs # avoid circular imports
        return_obj.id_ = obj.get_id()
        return_obj.version = obj.get_version() or cls._version
        return_obj.title = obj.get_Title()
        return_obj.description = StructuredText.from_obj(obj.get_Description())
        return_obj.short_description = StructuredText.from_obj(obj.get_Short_Description())
        return_obj.behavior = Behavior.from_obj(obj.get_Behavior())
        return_obj.related_ttps = RelatedTTPs.from_obj(obj.get_Related_TTPs())
        return_obj.information_source = InformationSource.from_obj(obj.get_Information_Source())
        
        return return_obj

    def to_dict(self):
        d = {}
        if self.id_:
            d['id'] = self.id_
        if self.version:
            d['version'] = self.version or self._version
        if self.title:
            d['title'] = self.title
        if self.description:
            d['description'] = self.description.to_dict()
        if self.short_description:
            d['short_description'] = self.short_description.to_dict()
        if self.behavior:
            d['behavior'] = self.behavior.to_dict()
        if self.related_ttps:
            d['related_ttps'] = self.related_ttps.to_dict()
        if self.information_source:
            d['information_source'] = self.information_source.to_dict()
        
        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()
        
        from .related_ttps import RelatedTTPs
        return_obj.id_ = dict_repr.get('id')
        return_obj.version = dict_repr.get('version', cls._version)
        return_obj.title = dict_repr.get('title')
        return_obj.description = StructuredText.from_dict(dict_repr.get('description'))
        return_obj.short_description = StructuredText.from_dict(dict_repr.get('short_description'))
        return_obj.behavior = Behavior.from_dict(dict_repr.get('behavior'))
        return_obj.related_ttps = RelatedTTPs.from_dict(dict_repr.get('related_ttps'))
        return_obj.information_source = InformationSource.from_dict(dict_repr.get('information_source'))
        
        return return_obj