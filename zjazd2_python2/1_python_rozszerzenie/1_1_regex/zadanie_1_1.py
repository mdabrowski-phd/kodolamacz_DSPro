# # 1. Znajdź w poniższym stringu numery telefonów

import re

string_to_clean = 'BTgMrF0npR665-5544-63BTgMrF0npR735-5520-51BTgMrF0npR885-5543-07BTgMrF0npR795-5583-74BTgMrF0npR505-' \
                  '5574-48BTgMrF0npR735-5514-34BTgMrF0npR455-5578-66BTgMrF0npR575-5596-20BTgMrF0npR605-5581-' \
                  '78BTgMrF0npR695-5575-18BTgMrF0npR885-5525-86BTgMrF0npR455-5535-05BTgMrF0npR785-5577-67BTgMr' \
                  'F0npR665-5533-11BTgMrF0npR695-5594-32BTgMrF0npR535-5540-51BTgMrF0npR785-5568-32BTgMrF0npR575-5592-' \
                  '96BTgMrF0npR455-5563-01BTgMrF0npR605-5537-21BTgMrF0npR455-5531-45BTgMrF0npR725-5534-83BTgMrF0np' \
                  'R885-5542-59BTgMrF0npR795-5516-02BTgMrF0npR695-5585-66BTgMrF0npR505-5572-18BTgMrF0npR735-5590-' \
                  '00BTgMrF0npR505-5543-71BTgMrF0npR735-5542-93BTgMrF0npR535-5563-43BTgMrF0npR665-5518-66BTgMrF0np' \
                  'R665-5538-23BTgMrF0npR605-5568-72BTgMrF0npR885-5549-15BTgMrF0npR455-5566-28BTgMrF0npR785-5580-' \
                  '92BTgMrF0npR695-5583-90BTgMrF0npR535-5561-47BTgMrF0npR505-5586-43BTgMrF0npR455-5550-78 '


moj_regex = re.compile(r'\d{3}-\d{4}-\d{2}')  # moj_regex = re.compile(r'\d+-\d+-\d+')
print(re.findall(moj_regex, string_to_clean))
print(len(re.findall(moj_regex, string_to_clean)))
