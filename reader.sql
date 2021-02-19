SELECT uuid, short_description
FROM cb_organizations
WHERE extract(year from founded_on) >= 1990 AND extract(year from founded_on) <2021
    AND num_cb_funding_rounds > 0
    AND short_description IS NOT NULL
