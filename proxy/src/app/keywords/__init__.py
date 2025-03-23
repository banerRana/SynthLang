"""
Keywords package for the SynthLang Proxy.

This package contains functionality for keyword detection and pattern matching.
"""
# Import default patterns to ensure they are registered
from app.keywords.registry import KEYWORD_REGISTRY, KeywordPattern, register_pattern
from app.keywords.default_patterns import register_default_patterns