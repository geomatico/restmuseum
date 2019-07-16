

def get_count_from_family_and_basis_of_record(family_id, basis_of_record):

    return """
    SELECT COUNT(),domain,kingdom,phylum,class,_order,family,familyid,genus,genusid 
    FROM mcnb_prod 
    WHERE familyid={familyid} AND basisofrecord={basisofrecord} 
    GROUP BY domain,kingdom,phylum,class,_order,family,familyid,genus,genusid 
    ORDER BY count() DESC
    """.format(familyid=family_id, basisofrecord=basis_of_record)
