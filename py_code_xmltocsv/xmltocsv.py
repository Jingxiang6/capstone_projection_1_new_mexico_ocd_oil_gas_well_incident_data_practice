import csv
import xml.etree.ElementTree as ET
# input xml file
inputs = 'C:/Users/Jing/Desktop/data_science/courses/capstone_topics/ocd/core/wellhistory/wellhistory.xml'
# column names of the table
header = ['api_st_cde', 'api_cnty_cde', 'api_well_idn', 'eff_dte', 'rec_termn_dte', 'ogrid_cde', 'well_name', 'prod_prop_idn',
'prop_fm_desc', 'well_nbr_idn', 'well_typ_cde', 'lease_typ_cde', 'ocd_district', 'last_apd_status', 'last_apd_apr_date',
'last_apd_cancel_date', 'latitude', 'longitude', 'datum', 'sdiv_twp_idn', 'sdiv_rng_idn', 'sdiv_sect_num', 'sdiv_unlt_idn', 
'ocd_unlt_idn', 'lot_idn', 'ftg_ns_num', 'ftg_ew_num', 'ns_cde', 'ew_cde', 'status', 'spud_dte', 'plug_dte', 'directional_status',
'completed_in_adjacent_state', 'elev_gl_num', 'dpth_tgt_num', 'dpth_tvd_num', 'dpth_mvd_num']
# create a .csv file to write into, row by row
with open('wellhistory.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # write in header in first line
    writer.writerow([i for i in header])
    row = [None] * 38
    for event, elem in ET.iterparse(inputs):
#        print(f'event = {event} elem = {elem}')
        assert event == 'end'
        if elem.tag.endswith('}api_st_cde'):
            row[0] = elem.text
        if elem.tag.endswith('}api_cnty_cde'):
            row[1] = elem.text
        if elem.tag.endswith('}api_well_idn'):
            row[2] = elem.text
        if elem.tag.endswith('}eff_dte'):
            row[3] = elem.text
        if elem.tag.endswith('}rec_termn_dte'):
            row[4] = elem.text
        if elem.tag.endswith('}ogrid_cde'):
            row[5] = elem.text
        if elem.tag.endswith('}well_name'):
            row[6] = elem.text
        if elem.tag.endswith('}prod_prop_idn'):
            row[7] = elem.text
        if elem.tag.endswith('}prop_fm_desc'):
            row[8] = elem.text
        if elem.tag.endswith('}well_nbr_idn'):
            row[9] = elem.text
        if elem.tag.endswith('}well_typ_cde'):
            row[10] = elem.text
        if elem.tag.endswith('}lease_typ_cde'):
            row[11] = elem.text
        if elem.tag.endswith('}ocd_district'):
            row[12] = elem.text    
        if elem.tag.endswith('}last_apd_status'):
            row[13] = elem.text  
        if elem.tag.endswith('}last_apd_apr_date'):
            row[14] = elem.text
        if elem.tag.endswith('}last_apd_cancel_date'):
            row[15] = elem.text
        if elem.tag.endswith('}latitude'):
            row[16] = elem.text
        if elem.tag.endswith('}longitude'):
            row[17] = elem.text
        if elem.tag.endswith('}datum'):
            row[18] = elem.text
        if elem.tag.endswith('}sdiv_twp_idn'):
            row[19] = elem.text
        if elem.tag.endswith('}sdiv_rng_idn'):
            row[20] = elem.text
        if elem.tag.endswith('}sdiv_sect_num'):
            row[21] = elem.text
        if elem.tag.endswith('}sdiv_unlt_idn'):
            row[22] = elem.text
        if elem.tag.endswith('}ocd_unlt_idn'):
            row[23] = elem.text
        if elem.tag.endswith('}lot_idn'):
            row[24] = elem.text
        if elem.tag.endswith('}ftg_ns_num'):
            row[25] = elem.text
        if elem.tag.endswith('}ftg_ew_num'):
            row[26] = elem.text
        if elem.tag.endswith('}ns_cde'):
            row[27] = elem.text
        if elem.tag.endswith('}ew_cde'):
            row[28] = elem.text
        if elem.tag.endswith('}status'):
            row[29] = elem.text
        if elem.tag.endswith('}spud_dte'):
            row[30] = elem.text
        if elem.tag.endswith('}plug_dte'):
            row[31] = elem.text
        if elem.tag.endswith('}directional_status'):
            row[32] = elem.text
        if elem.tag.endswith('}completed_in_adjacent_state'):
            row[33] = elem.text
        if elem.tag.endswith('}elev_gl_num'):
            row[34] = elem.text  
        if elem.tag.endswith('}dpth_tgt_num'):
            row[35] = elem.text
        if elem.tag.endswith('}dpth_tvd_num'):
            row[36] = elem.text
        if elem.tag.endswith('}dpth_mvd_num'):
            row[37] = elem.text       
        if elem.tag.endswith('}wellhistory'):
            writer.writerow([i for i in row])
            elem.clear()
   