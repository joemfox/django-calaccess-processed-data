#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Proxy models for augmenting our source data tables with methods useful for processing.
"""
from .calaccess_raw import RawFilerToFilerTypeCdManager
from .calaccess_scraped import (
    ScrapedCandidateProxy,
    ScrapedIncumbentProxy,
    ScrapedCandidateElectionProxy,
    ScrapedIncumbentElectionProxy,
    ScrapedPropositionProxy,
    ScrapedPropositionElectionProxy
)
from .opencivicdata import (
    OCDCandidacyProxy,
    OCDDivisionProxy,
    OCDElectionProxy,
    OCDOrganizationProxy,
    OCDPartyProxy,
    OCDPersonProxy,
    OCDPostProxy,
    OCDRunoffProxy,
)


__all__ = (
    'RawFilerToFilerTypeCdManager',
    'ScrapedCandidateProxy',
    'ScrapedCandidateElectionProxy',
    'ScrapedIncumbentProxy',
    'ScrapedIncumbentElectionProxy',
    'ScrapedPropositionProxy',
    'ScrapedPropositionElectionProxy',
    'OCDCandidacyProxy',
    'OCDDivisionProxy',
    'OCDElectionProxy',
    'OCDOrganizationProxy',
    'OCDPartyProxy',
    'OCDPersonProxy',
    'OCDPostProxy',
    'OCDRunoffProxy',
)
