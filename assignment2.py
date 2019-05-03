#! /usr/bin/env python3

import vcf

import os

__author__ = 'Sarah Meitz'


class Assignment2:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)

        self.chr22 = os.path.join(os.getcwd(), "chr22.vcf")
        self.chr21 = os.path.join(os.getcwd(), "chr21.vcf")


    def get_average_quality_of_file(self):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''
        vcf_chr22 = vcf.Reader(open(self.chr22), "r")
        i = 0
        averageQ = 0

        for record in vcf_chr22:
            i += 1
            averageQ += record.QUAL
        phred = averageQ / i

        print("Average PHRED quality of all variants is: ", str(phred))

        
        
    def get_total_number_of_variants_of_file(self):
        '''
        Get the total number of variants
        :return: total number of variants
        '''
        vcf_chr22 = vcf.Reader(open(self.chr22), "r")
        i = 0
        for record in vcf_chr22:
            i += 1
        print("Total number of variants: ", i)
    
    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return: 
        '''
        # no idea where this information is
        # should be in the header but it isn't

    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''
        # no idea where this information is 
        # should be in the header but it isn't

        
    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs
        :return:
        '''
        vcf_chr22 = vcf.Reader(open(self.chr22), "r")
        i = 0
        for record in vcf_chr22:
            if record.is_indel:
                i += 1
        print("Number of identified INDELs: ", i)
        

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        '''
        vcf_chr22 = vcf.Reader(open(self.chr22), "r")
        i = 0
        # According to documentation attribute .is_snp is similar to snv
        for record in vcf_chr22:
            if record.is_snp:
                i += 1
        print("Number of SNVs: ", i)
        
    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return: 
        '''
        vcf_chr22 = vcf.Reader(open(self.chr22), "r")
        i = 0
        for record in vcf_chr22:
            if record.num_het:
                i += 1
        print("Number of heterozygous variants: ", i)
        
    
    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''
        # combine both files - not done with vcf writer as there are problems with chr21 file
        files = [self.chr22, self.chr21]
        with open("chr21_chr22.vcf", "w") as outfile:
            for filenames in files:
                with open(filenames) as infile:
                    for line in infile:
                        outfile.write(line)

        combined = os.path.join(os.getcwd(), "chr21_chr22.vcf")
        vcf_combined = vcf.Reader(open(combined), "r")
        i = 0
        for record in vcf_combined:
             i += 1
        print("Total number of variants in chr21 + chr22: ", i)
        

    def print_summary(self):
        print("Print all results here")
        self.get_average_quality_of_file()
        self.get_total_number_of_variants_of_file()
        #self.get_variant_caller_of_vcf()
        #self.get_human_reference_version()
        self.get_number_of_indels()
        self.get_number_of_snvs()
        self.get_number_of_heterozygous_variants()
        self.merge_chrs_into_one_vcf()

    
    
def main():
    print("Assignment 2")
    assignment2 = Assignment2()
    assignment2.print_summary()
    print("Done with assignment 2")
        
        
if __name__ == '__main__':
    main()
   
    



