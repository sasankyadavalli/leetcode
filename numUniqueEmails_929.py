class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for i in emails:
            local, domain = i.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            if '.' in local:
                local = local.replace('.', '')

            seen.add(local+'@'+domain)
            
        return len(seen)