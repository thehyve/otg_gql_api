from otg_scan_all_gecko import GeckoScanner


scanner = GeckoScanner('http://genetics-api.opentargets.io/graphql')


discovered_genes = set()
discovered_studies = set()
discovered_variants = set()


for gecko in scanner.scan_all_gecko():
    if 'data' in gecko and 'gecko' in gecko['data'] and gecko['data']['gecko'] is not None:
        gecko = gecko['data']['gecko']
        if 'genes' in gecko:
            genes = gecko['genes']
            for gene in genes:
                if not gene['id'] in discovered_genes:
                    discovered_genes.add(gene['id'])
                    print('gene', gene['id'], sep='\t')
        if 'tagVariants' in gecko:
            tag_variants = gecko['tagVariants']
            for variant in tag_variants:
                if not variant['rsId'] in discovered_genes:
                    discovered_variants.add(variant['rsId'])
                    print('variant', variant['rsId'], sep='\t')
        if 'indexVariants' in gecko:
            index_variants = gecko['indexVariants']
            for variant in index_variants:
                if not variant['rsId'] in discovered_genes:
                    discovered_variants.add(variant['rsId'])
                    print('variant', variant['rsId'], sep='\t')
        if 'studies' in gecko:
            studies = gecko['studies']
            for study in studies:
                if not study['studyId'] in discovered_genes:
                    discovered_studies.add(study['studyId'])
                    print('study', study['studyId'], sep='\t')
