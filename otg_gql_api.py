import requests
from json.decoder import JSONDecodeError
import sys

class NotOkStatus(Exception):
    pass

class OtgGqlApi:

    def __init__(self, api_url='http://genetics-api.opentargets.io/graphql'):
        self.api_url = api_url

    def _run_query(self, query):
        request = requests.post(self.api_url, json={'query': query})
        if request.status_code == 200:
            try:
                return request.json()
            except JSONDecodeError as e:
                print('Got unparsable json', request.text, file=sys.stderr)
                raise e
        else:
            raise NotOkStatus("Query failed to run by returning code of {}. {}: {}".format(request.status_code, query, request.text))

    _gecko_query = '''\
        query {
          gecko(chromosome: "%(chromosome)s", start: %(start)s, end: %(end)s) {
            genes {
              id
              symbol
              description
              chromosome
              start
              end
              tss
              bioType
              fwdStrand
              exons
            }
            tagVariants {
              id
              idB37
              rsId
              chromosome
              position
              chromosomeB37
              positionB37
              refAllele
              altAllele
              nearestGene {
                id
                symbol
                description
                chromosome
                start
                end
                tss
                bioType
                fwdStrand
                exons
              }
              nearestGeneDistance
              nearestCodingGene {
                id
                symbol
                description
                chromosome
                start
                end
                tss
                bioType
                fwdStrand
                exons
              }
              nearestCodingGeneDistance
              mostSevereConsequence
              caddRaw
              caddPhred
              gnomadAFR
              gnomadAMR
              gnomadASJ
              gnomadEAS
              gnomadFIN
              gnomadNFE
              gnomadNFEEST
              gnomadNFENWE
              gnomadNFESEU
              gnomadNFEONF
              gnomadOTH
            }
            indexVariants {
              id
              idB37
              rsId
              chromosome
              position
              chromosomeB37
              positionB37
              refAllele
              altAllele
              nearestGene {
                id
                symbol
                description
                chromosome
                start
                end
                tss
                bioType
                fwdStrand
                exons
              }
              nearestGeneDistance
              nearestCodingGene {
                id
                symbol
                description
                chromosome
                start
                end
                tss
                bioType
                fwdStrand
                exons
              }
              nearestCodingGeneDistance
              mostSevereConsequence
              caddRaw
              caddPhred
              gnomadAFR
              gnomadAMR
              gnomadASJ
              gnomadEAS
              gnomadFIN
              gnomadNFE
              gnomadNFEEST
              gnomadNFENWE
              gnomadNFESEU
              gnomadNFEONF
              gnomadOTH
            }
            studies {
              studyId
              traitReported
              traitEfos
              pmid
              pubDate
              pubJournal
              pubTitle
              pubAuthor
              hasSumsStats
              ancestryInitial
              ancestryReplication
              nInitial
              nReplication
              nCases
              nTotal
              traitCategory
              numAssocLoci
            }
            geneTagVariants {
              geneId
              tagVariantId
              overallScore
            }
            tagVariantIndexVariantStudies {
              tagVariantId
              indexVariantId
              studyId
              posteriorProbability
              pval
              pvalMantissa
              pvalExponent
              oddsRatio
              oddsRatioCILower
              oddsRatioCIUpper
              beta
              betaCILower
              betaCIUpper
              direction
            }
          }
        }
    '''

    def query_gecko(self, chromosome, start, end):
        return self._run_query(self._gecko_query % { "chromosome": chromosome, "start": start, "end": end })


if __name__ == '__main__':
    gecko = OtgGqlApi().query_gecko(chromosome='1', start=0, end=2000000)
    print(gecko)

