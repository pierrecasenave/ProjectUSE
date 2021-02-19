SELECT cb_organizations.uuid as org_uuid, cb_organizations.name as name,
    founded_on, CAST(extract(year from founded_on) as INTEGER) as year_founded,
    status, primary_role, category_list, short_description, description, num_cb_funding_rounds as funding_rounds,
    total_funding_usd
FROM cb_organizations
LEFT JOIN cb_organization_descriptions
ON cb_organizations.uuid=cb_organization_descriptions.uuid
WHERE extract(year from founded_on) >= 1990 AND extract(year from founded_on) <2021
    AND num_cb_funding_rounds > 0
    AND short_description IS NOT NULL
