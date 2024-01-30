    treeType = treeType.lower()
    if treeType not in treeBuilderCache:
        if treeType == "dom":
            from . import dom
            # Come up with a sane default (pref. from the stdlib)
            if implementation is None:
                from xml.dom import minidom
                implementation = minidom
            # NEVER cache here, caching is done in the dom submodule
            return dom.getDomModule(implementation, **kwargs).TreeBuilder
        elif treeType == "lxml":
            from . import etree_lxml
            treeBuilderCache[treeType] = etree_lxml.TreeBuilder
        elif treeType == "etree":
            from . import etree
            if implementation is None:
                implementation = default_etree
            # NEVER cache here, caching is done in the etree submodule
            return etree.getETreeModule(implementation, **kwargs).TreeBuilder
        else:
            raise ValueError("""Unrecognised treebuilder "%s" """ % treeType)
    return treeBuilderCache.get(treeType)
lambda 