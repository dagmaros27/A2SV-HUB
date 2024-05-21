# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visited_domain = defaultdict(int)
        
        for cp in cpdomains:
            count, domain = cp.split()
            count = int(count)
            visited_domain[domain] += count
            subdomains = domain.split('.')
            for i in range(1, len(subdomains)):
                visited_domain['.'.join(subdomains[i:])] += count
        
        result = []
        for domain, count in visited_domain.items():
            result.append(f"{count} {domain}")
        
        return result