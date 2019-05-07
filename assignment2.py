#! /usr/bin/env python3

import vcf
import os
import subprocess

__author__ = 'Sarah Meitz'


class Assignment2:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)

        self.chr22 = os.path.join(os.getcwd(), "chr22_new.vcf")
        self.chr21 = os.path.join(os.getcwd(), "chr21_new.vcf")

        if not os.path.isfile(self.chr22):
            subprocess.call(["wget", "http://hmd.ait.ac.at/medgen2019/chr21_new.vcf"])
        if not os.path.isfile(self.chr21):
            subprocess.call(["wget", "http://hmd.ait.ac.at/medgen2019/chr22_new.vcf"])


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

        vcf_chr22 = vcf.Reader(open(self.chr22), "r")
        for record in vcf_chr22:
           vcaller = record.INFO["callsetnames"]
        print("Variant caller name: ", vcaller[1])

    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''
        vcf_chr22 = vcf.Reader(open(self.chr22), "r")
        for record in vcf_chr22:
            href = record.INFO

        print("Human reference genome: ", href["difficultregion"][0])

        
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


        vcf_chr21 = vcf.Reader(open(self.chr21), "r")
        vcf_chr22 = vcf.Reader(open(self.chr22), "r")
        vcf_Writer = vcf.Writer(open("chr21_chr22.vcf", "w"), vcf_chr22)
        for record in vcf_chr22:
            vcf_Writer.write_record(record)
        for record in vcf_chr21:
            vcf_Writer.write_record(record)

        combined = os.path.join(os.getcwd(), "chr21_chr22.vcf")
        vcf_combined = vcf.Reader(open(combined), "r")
        i = 0
        for record in vcf_combined:
             i += 1
        print("Total number of variants in chr21 + chr22: ", i)
        

    def print_summary(self):

        self.get_average_quality_of_file()
        self.get_total_number_of_variants_of_file()
        self.get_variant_caller_of_vcf()
        self.get_human_reference_version()
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
   
    



