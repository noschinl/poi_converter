"""
tagfilter
checks which entries in input file should be forwarded to output database
"""
class TagFilter:
    def __init__(self, filter_file):
        # Dictionary of the valid tags. The key is the tag, the value the inverse priority (lower values mean higher priority)
        self.valid_tags = {}
        with open(filter_file,'r') as f:
            line = f.readline()
            prio = 0
            while line:
                if not line.startswith('#') and len(line) > 2:
                    tag = line.strip().split('=')
                    self.valid_tags[(tag[0],tag[1])] = prio
                    prio += 1
                line = f.readline()            

    """
    returns the matching tag with the highest priority (or None)
    """
    def tag_matched(self, tags):
        matched_tag = None
        matched_prio = None
        for tag in tags:
            prio = self.valid_tags.get(tag)
            if prio is not None and (matched_prio is None or prio < matched_prio):
                matched_tag = tag
                matched_priority = prio
        return matched_tag
