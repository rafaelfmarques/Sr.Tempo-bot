from fuzzywuzzy import fuzz
from fuzzywuzzy import process

cidades = []

city = '''Alta Floresta D'Oeste-RO&
Alto Alegre dos Parecis-RO&
Alto Paraíso-RO&
Alvorada D'Oeste-RO&
Ariquemes-RO&
Buritis-RO&
Cabixi-RO&
Cacaulândia-RO&
Cacoal-RO&
Campo Novo de Rondônia-RO&
Candeias do Jamari-RO&
Castanheiras-RO&
Cerejeiras-RO&
Chupinguaia-RO&
Colorado do Oeste-RO&
Corumbiara-RO&
Costa Marques-RO&
Cujubim-RO&
Espigão D'Oeste-RO&
Governador Jorge Teixeira-RO&
Guajará-Mirim-RO&
Itapuã do Oeste-RO&
Jaru-RO&
Ji-Paraná-RO&
Machadinho D'Oeste-RO&
Ministro Andreazza-RO&
Mirante da Serra-RO&
Monte Negro-RO&
Nova Brasilândia D'Oeste-RO&
Nova Mamoré-RO&
Nova União-RO&
Novo Horizonte do Oeste-RO&
Ouro Preto do Oeste-RO&
Parecis-RO&
Pimenta Bueno-RO&
Pimenteiras do Oeste-RO&
Porto Velho-RO&
Presidente Médici-RO&
Primavera de Rondônia-RO&
Rio Crespo-RO&
Rolim de Moura-RO&
Santa Luzia D'Oeste-RO&
São Felipe D'Oeste-RO&
São Francisco do Guaporé-RO&
São Miguel do Guaporé-RO&
Seringueiras-RO&
Teixeirópolis-RO&
Theobroma-RO&
Urupá-RO&
Vale do Anari-RO&
Vale do Paraíso-RO&
Vilhena-RO&
Acrelândia-AC&
Assis Brasil-AC&
Brasiléia-AC&
Bujari-AC&
Capixaba-AC&
Cruzeiro do Sul-AC&
Epitaciolândia-AC&
Feijó-AC&
Jordão-AC&
Mâncio Lima-AC&
Manoel Urbano-AC&
Marechal Thaumaturgo-AC&
Plácido de Castro-AC&
Porto Acre-AC&
Porto Walter-AC&
Rio Branco-AC&
Rodrigues Alves-AC&
Santa Rosa do Purus-AC&
Sena Madureira-AC&
Senador Guiomard-AC&
Tarauacá-AC&
Xapuri-AC&
Alvarães-AM&
Amaturá-AM&
Anamã-AM&
Anori-AM&
Apuí-AM&
Atalaia do Norte-AM&
Autazes-AM&
Barcelos-AM&
Barreirinha-AM&
Benjamin Constant-AM&
Beruri-AM&
Boa Vista do Ramos-AM&
Boca do Acre-AM&
Borba-AM&
Caapiranga-AM&
Canutama-AM&
Carauari-AM&
Careiro-AM&
Careiro da Várzea-AM&
Coari-AM&
Codajás-AM&
Eirunepé-AM&
Envira-AM&
Fonte Boa-AM&
Guajará-AM&
Humaitá-AM&
Ipixuna-AM&
Iranduba-AM&
Itacoatiara-AM&
Itamarati-AM&
Itapiranga-AM&
Japurá-AM&
Juruá-AM&
Jutaí-AM&
Lábrea-AM&
Manacapuru-AM&
Manaquiri-AM&
Manaus-AM&
Manicoré-AM&
Maraã-AM&
Maués-AM&
Nhamundá-AM&
Nova Olinda do Norte-AM&
Novo Airão-AM&
Novo Aripuanã-AM&
Parintins-AM&
Pauini-AM&
Presidente Figueiredo-AM&
Rio Preto da Eva-AM&
Santa Isabel do Rio Negro-AM&
Santo Antônio do Içá-AM&
São Gabriel da Cachoeira-AM&
São Paulo de Olivença-AM&
São Sebastião do Uatumã-AM&
Silves-AM&
Tabatinga-AM&
Tapauá-AM&
Tefé-AM&
Tonantins-AM&
Uarini-AM&
Urucará-AM&
Urucurituba-AM&
Alto Alegre-RR&
Amajari-RR&
Boa Vista-RR&
Bonfim-RR&
Cantá-RR&
Caracaraí-RR&
Caroebe-RR&
Iracema-RR&
Mucajaí-RR&
Normandia-RR&
Pacaraima-RR&
Rorainópolis-RR&
São João da Baliza-RR&
São Luiz-RR&
Uiramutã-RR&
Abaetetuba-PA&
Abel Figueiredo-PA&
Acará-PA&
Afuá-PA&
Água Azul do Norte-PA&
Alenquer-PA&
Almeirim-PA&
Altamira-PA&
Anajás-PA&
Ananindeua-PA&
Anapu-PA&
Augusto Corrêa-PA&
Aurora do Pará-PA&
Aveiro-PA&
Bagre-PA&
Baião-PA&
Bannach-PA&
Barcarena-PA&
Belém-PA&
Belterra-PA&
Benevides-PA&
Bom Jesus do Tocantins-PA&
Bonito-PA&
Bragança-PA&
Brasil Novo-PA&
Brejo Grande do Araguaia-PA&
Breu Branco-PA&
Breves-PA&
Bujaru-PA&
Cachoeira do Arari-PA&
Cachoeira do Piriá-PA&
Cametá-PA&
Canaã dos Carajás-PA&
Capanema-PA&
Capitão Poço-PA&
Castanhal-PA&
Chaves-PA&
Colares-PA&
Conceição do Araguaia-PA&
Concórdia do Pará-PA&
Cumaru do Norte-PA&
Curionópolis-PA&
Curralinho-PA&
Curuá-PA&
Curuçá-PA&
Dom Eliseu-PA&
Eldorado dos Carajás-PA&
Faro-PA&
Floresta do Araguaia-PA&
Garrafão do Norte-PA&
Goianésia do Pará-PA&
Gurupá-PA&
Igarapé-Açu-PA&
Igarapé-Miri-PA&
Inhangapi-PA&
Ipixuna do Pará-PA&
Irituia-PA&
Itaituba-PA&
Itupiranga-PA&
Jacareacanga-PA&
Jacundá-PA&
Juruti-PA&
Limoeiro do Ajuru-PA&
Mãe do Rio-PA&
Magalhães Barata-PA&
Marabá-PA&
Maracanã-PA&
Marapanim-PA&
Marituba-PA&
Medicilândia-PA&
Melgaço-PA&
Mocajuba-PA&
Moju-PA&
Monte Alegre-PA&
Muaná-PA&
Nova Esperança do Piriá-PA&
Nova Ipixuna-PA&
Nova Timboteua-PA&
Novo Progresso-PA&
Novo Repartimento-PA&
Óbidos-PA&
Oeiras do Pará-PA&
Oriximiná-PA&
Ourém-PA&
Ourilândia do Norte-PA&
Pacajá-PA&
Palestina do Pará-PA&
Paragominas-PA&
Parauapebas-PA&
Pau D'Arco-PA&
Peixe-Boi-PA&
Piçarra-PA&
Placas-PA&
Ponta de Pedras-PA&
Portel-PA&
Porto de Moz-PA&
Prainha-PA&
Primavera-PA&
Quatipuru-PA&
Redenção-PA&
Rio Maria-PA&
Rondon do Pará-PA&
Rurópolis-PA&
Salinópolis-PA&
Salvaterra-PA&
Santa Bárbara do Pará-PA&
Santa Cruz do Arari-PA&
Santa Isabel do Pará-PA&
Santa Luzia do Pará-PA&
Santa Maria das Barreiras-PA&
Santa Maria do Pará-PA&
Santana do Araguaia-PA&
Santarém-PA&
Santarém Novo-PA&
Santo Antônio do Tauá-PA&
São Caetano de Odivelas-PA&
São Domingos do Araguaia-PA&
São Domingos do Capim-PA&
São Félix do Xingu-PA&
São Francisco do Pará-PA&
São Geraldo do Araguaia-PA&
São João da Ponta-PA&
São João de Pirabas-PA&
São João do Araguaia-PA&
São Miguel do Guamá-PA&
São Sebastião da Boa Vista-PA&
Sapucaia-PA&
Senador José Porfírio-PA&
Soure-PA&
Tailândia-PA&
Terra Alta-PA&
Terra Santa-PA&
Tomé-Açu-PA&
Tracuateua-PA&
Trairão-PA&
Tucumã-PA&
Tucuruí-PA&
Ulianópolis-PA&
Uruará-PA&
Vigia-PA&
Viseu-PA&
Vitória do Xingu-PA&
Xinguara-PA&
Amapá-AP&
Calçoene-AP&
Cutias-AP&
Ferreira Gomes-AP&
Itaubal-AP&
Laranjal do Jari-AP&
Macapá-AP&
Mazagão-AP&
Oiapoque-AP&
Pedra Branca do Amapari-AP&
Porto Grande-AP&
Pracuúba-AP&
Santana-AP&
Serra do Navio-AP&
Tartarugalzinho-AP&
Vitória do Jari-AP&
Abreulândia-TO&
Aguiarnópolis-TO&
Aliança do Tocantins-TO&
Almas-TO&
Alvorada-TO&
Ananás-TO&
Angico-TO&
Aparecida do Rio Negro-TO&
Aragominas-TO&
Araguacema-TO&
Araguaçu-TO&
Araguaína-TO&
Araguanã-TO&
Araguatins-TO&
Arapoema-TO&
Arraias-TO&
Augustinópolis-TO&
Aurora do Tocantins-TO&
Axixá do Tocantins-TO&
Babaçulândia-TO&
Bandeirantes do Tocantins-TO&
Barra do Ouro-TO&
Barrolândia-TO&
Bernardo Sayão-TO&
Bom Jesus do Tocantins-TO&
Brasilândia do Tocantins-TO&
Brejinho de Nazaré-TO&
Buriti do Tocantins-TO&
Cachoeirinha-TO&
Campos Lindos-TO&
Cariri do Tocantins-TO&
Carmolândia-TO&
Carrasco Bonito-TO&
Caseara-TO&
Centenário-TO&
Chapada da Natividade-TO&
Chapada de Areia-TO&
Colinas do Tocantins-TO&
Colméia-TO&
Combinado-TO&
Conceição do Tocantins-TO&
Couto de Magalhães-TO&
Cristalândia-TO&
Crixás do Tocantins-TO&
Darcinópolis-TO&
Dianópolis-TO&
Divinópolis do Tocantins-TO&
Dois Irmãos do Tocantins-TO&
Dueré-TO&
Esperantina-TO&
Fátima-TO&
Figueirópolis-TO&
Filadélfia-TO&
Formoso do Araguaia-TO&
Fortaleza do Tabocão-TO&
Goianorte-TO&
Goiatins-TO&
Guaraí-TO&
Gurupi-TO&
Ipueiras-TO&
Itacajá-TO&
Itaguatins-TO&
Itapiratins-TO&
Itaporã do Tocantins-TO&
Jaú do Tocantins-TO&
Juarina-TO&
Lagoa da Confusão-TO&
Lagoa do Tocantins-TO&
Lajeado-TO&
Lavandeira-TO&
Lizarda-TO&
Luzinópolis-TO&
Marianópolis do Tocantins-TO&
Mateiros-TO&
Maurilândia do Tocantins-TO&
Miracema do Tocantins-TO&
Miranorte-TO&
Monte do Carmo-TO&
Monte Santo do Tocantins-TO&
Muricilândia-TO&
Natividade-TO&
Nazaré-TO&
Nova Olinda-TO&
Nova Rosalândia-TO&
Novo Acordo-TO&
Novo Alegre-TO&
Novo Jardim-TO&
Oliveira de Fátima-TO&
Palmas-TO&
Palmeirante-TO&
Palmeiras do Tocantins-TO&
Palmeirópolis-TO&
Paraíso do Tocantins-TO&
Paranã-TO&
Pau D'Arco-TO&
Pedro Afonso-TO&
Peixe-TO&
Pequizeiro-TO&
Pindorama do Tocantins-TO&
Piraquê-TO&
Pium-TO&
Ponte Alta do Bom Jesus-TO&
Ponte Alta do Tocantins-TO&
Porto Alegre do Tocantins-TO&
Porto Nacional-TO&
Praia Norte-TO&
Presidente Kennedy-TO&
Pugmil-TO&
Recursolândia-TO&
Riachinho-TO&
Rio da Conceição-TO&
Rio dos Bois-TO&
Rio Sono-TO&
Sampaio-TO&
Sandolândia-TO&
Santa Fé do Araguaia-TO&
Santa Maria do Tocantins-TO&
Santa Rita do Tocantins-TO&
Santa Rosa do Tocantins-TO&
Santa Tereza do Tocantins-TO&
Santa Terezinha do Tocantins-TO&
São Bento do Tocantins-TO&
São Félix do Tocantins-TO&
São Miguel do Tocantins-TO&
São Salvador do Tocantins-TO&
São Sebastião do Tocantins-TO&
São Valério da Natividade-TO&
Silvanópolis-TO&
Sítio Novo do Tocantins-TO&
Sucupira-TO&
Taguatinga-TO&
Taipas do Tocantins-TO&
Talismã-TO&
Tocantínia-TO&
Tocantinópolis-TO&
Tupirama-TO&
Tupiratins-TO&
Wanderlândia-TO&
Xambioá-TO&
Açailândia-MA&
Afonso Cunha-MA&
Água Doce do Maranhão-MA&
Alcântara-MA&
Aldeias Altas-MA&
Altamira do Maranhão-MA&
Alto Alegre do Maranhão-MA&
Alto Alegre do Pindaré-MA&
Alto Parnaíba-MA&
Amapá do Maranhão-MA&
Amarante do Maranhão-MA&
Anajatuba-MA&
Anapurus-MA&
Apicum-Açu-MA&
Araguanã-MA&
Araioses-MA&
Arame-MA&
Arari-MA&
Axixá-MA&
Bacabal-MA&
Bacabeira-MA&
Bacuri-MA&
Bacurituba-MA&
Balsas-MA&
Barão de Grajaú-MA&
Barra do Corda-MA&
Barreirinhas-MA&
Bela Vista do Maranhão-MA&
Belágua-MA&
Benedito Leite-MA&
Bequimão-MA&
Bernardo do Mearim-MA&
Boa Vista do Gurupi-MA&
Bom Jardim-MA&
Bom Jesus das Selvas-MA&
Bom Lugar-MA&
Brejo-MA&
Brejo de Areia-MA&
Buriti-MA&
Buriti Bravo-MA&
Buriticupu-MA&
Buritirana-MA&
Cachoeira Grande-MA&
Cajapió-MA&
Cajari-MA&
Campestre do Maranhão-MA&
Cândido Mendes-MA&
Cantanhede-MA&
Capinzal do Norte-MA&
Carolina-MA&
Carutapera-MA&
Caxias-MA&
Cedral-MA&
Central do Maranhão-MA&
Centro do Guilherme-MA&
Centro Novo do Maranhão-MA&
Chapadinha-MA&
Cidelândia-MA&
Codó-MA&
Coelho Neto-MA&
Colinas-MA&
Conceição do Lago-Açu-MA&
Coroatá-MA&
Cururupu-MA&
Davinópolis-MA&
Dom Pedro-MA&
Duque Bacelar-MA&
Esperantinópolis-MA&
Estreito-MA&
Feira Nova do Maranhão-MA&
Fernando Falcão-MA&
Formosa da Serra Negra-MA&
Fortaleza dos Nogueiras-MA&
Fortuna-MA&
Godofredo Viana-MA&
Gonçalves Dias-MA&
Governador Archer-MA&
Governador Edison Lobão-MA&
Governador Eugênio Barros-MA&
Governador Luiz Rocha-MA&
Governador Newton Bello-MA&
Governador Nunes Freire-MA&
Graça Aranha-MA&
Grajaú-MA&
Guimarães-MA&
Humberto de Campos-MA&
Icatu-MA&
Igarapé do Meio-MA&
Igarapé Grande-MA&
Imperatriz-MA&
Itaipava do Grajaú-MA&
Itapecuru Mirim-MA&
Itinga do Maranhão-MA&
Jatobá-MA&
Jenipapo dos Vieiras-MA&
João Lisboa-MA&
Joselândia-MA&
Junco do Maranhão-MA&
Lago da Pedra-MA&
Lago do Junco-MA&
Lago dos Rodrigues-MA&
Lago Verde-MA&
Lagoa do Mato-MA&
Lagoa Grande do Maranhão-MA&
Lajeado Novo-MA&
Lima Campos-MA&
Loreto-MA&
Luís Domingues-MA&
Magalhães de Almeida-MA&
Maracaçumé-MA&
Marajá do Sena-MA&
Maranhãozinho-MA&
Mata Roma-MA&
Matinha-MA&
Matões-MA&
Matões do Norte-MA&
Milagres do Maranhão-MA&
Mirador-MA&
Miranda do Norte-MA&
Mirinzal-MA&
Monção-MA&
Montes Altos-MA&
Morros-MA&
Nina Rodrigues-MA&
Nova Colinas-MA&
Nova Iorque-MA&
Nova Olinda do Maranhão-MA&
Olho d'Água das Cunhãs-MA&
Olinda Nova do Maranhão-MA&
Paço do Lumiar-MA&
Palmeirândia-MA&
Paraibano-MA&
Parnarama-MA&
Passagem Franca-MA&
Pastos Bons-MA&
Paulino Neves-MA&
Paulo Ramos-MA&
Pedreiras-MA&
Pedro do Rosário-MA&
Penalva-MA&
Peri Mirim-MA&
Peritoró-MA&
Pindaré-Mirim-MA&
Pinheiro-MA&
Pio XII-MA&
Pirapemas-MA&
Poção de Pedras-MA&
Porto Franco-MA&
Porto Rico do Maranhão-MA&
Presidente Dutra-MA&
Presidente Juscelino-MA&
Presidente Médici-MA&
Presidente Sarney-MA&
Presidente Vargas-MA&
Primeira Cruz-MA&
Raposa-MA&
Riachão-MA&
Ribamar Fiquene-MA&
Rosário-MA&
Sambaíba-MA&
Santa Filomena do Maranhão-MA&
Santa Helena-MA&
Santa Inês-MA&
Santa Luzia-MA&
Santa Luzia do Paruá-MA&
Santa Quitéria do Maranhão-MA&
Santa Rita-MA&
Santana do Maranhão-MA&
Santo Amaro do Maranhão-MA&
Santo Antônio dos Lopes-MA&
São Benedito do Rio Preto-MA&
São Bento-MA&
São Bernardo-MA&
São Domingos do Azeitão-MA&
São Domingos do Maranhão-MA&
São Félix de Balsas-MA&
São Francisco do Brejão-MA&
São Francisco do Maranhão-MA&
São João Batista-MA&
São João do Carú-MA&
São João do Paraíso-MA&
São João do Soter-MA&
São João dos Patos-MA&
São José de Ribamar-MA&
São José dos Basílios-MA&
São Luís-MA&
São Luís Gonzaga do Maranhão-MA&
São Mateus do Maranhão-MA&
São Pedro da Água Branca-MA&
São Pedro dos Crentes-MA&
São Raimundo das Mangabeiras-MA&
São Raimundo do Doca Bezerra-MA&
São Roberto-MA&
São Vicente Ferrer-MA&
Satubinha-MA&
Senador Alexandre Costa-MA&
Senador La Rocque-MA&
Serrano do Maranhão-MA&
Sítio Novo-MA&
Sucupira do Norte-MA&
Sucupira do Riachão-MA&
Tasso Fragoso-MA&
Timbiras-MA&
Timon-MA&
Trizidela do Vale-MA&
Tufilândia-MA&
Tuntum-MA&
Turiaçu-MA&
Turilândia-MA&
Tutóia-MA&
Urbano Santos-MA&
Vargem Grande-MA&
Viana-MA&
Vila Nova dos Martírios-MA&
Vitória do Mearim-MA&
Vitorino Freire-MA&
Zé Doca-MA&
Acauã-PI&
Agricolândia-PI&
Água Branca-PI&
Alagoinha do Piauí-PI&
Alegrete do Piauí-PI&
Alto Longá-PI&
Altos-PI&
Alvorada do Gurguéia-PI&
Amarante-PI&
Angical do Piauí-PI&
Anísio de Abreu-PI&
Antônio Almeida-PI&
Aroazes-PI&
Aroeiras do Itaim-PI&
Arraial-PI&
Assunção do Piauí-PI&
Avelino Lopes-PI&
Baixa Grande do Ribeiro-PI&
Barra D'Alcântara-PI&
Barras-PI&
Barreiras do Piauí-PI&
Barro Duro-PI&
Batalha-PI&
Bela Vista do Piauí-PI&
Belém do Piauí-PI&
Beneditinos-PI&
Bertolínia-PI&
Betânia do Piauí-PI&
Boa Hora-PI&
Bocaina-PI&
Bom Jesus-PI&
Bom Princípio do Piauí-PI&
Bonfim do Piauí-PI&
Boqueirão do Piauí-PI&
Brasileira-PI&
Brejo do Piauí-PI&
Buriti dos Lopes-PI&
Buriti dos Montes-PI&
Cabeceiras do Piauí-PI&
Cajazeiras do Piauí-PI&
Cajueiro da Praia-PI&
Caldeirão Grande do Piauí-PI&
Campinas do Piauí-PI&
Campo Alegre do Fidalgo-PI&
Campo Grande do Piauí-PI&
Campo Largo do Piauí-PI&
Campo Maior-PI&
Canavieira-PI&
Canto do Buriti-PI&
Capitão de Campos-PI&
Capitão Gervásio Oliveira-PI&
Caracol-PI&
Caraúbas do Piauí-PI&
Caridade do Piauí-PI&
Castelo do Piauí-PI&
Caxingó-PI&
Cocal-PI&
Cocal de Telha-PI&
Cocal dos Alves-PI&
Coivaras-PI&
Colônia do Gurguéia-PI&
Colônia do Piauí-PI&
Conceição do Canindé-PI&
Coronel José Dias-PI&
Corrente-PI&
Cristalândia do Piauí-PI&
Cristino Castro-PI&
Curimatá-PI&
Currais-PI&
Curral Novo do Piauí-PI&
Curralinhos-PI&
Demerval Lobão-PI&
Dirceu Arcoverde-PI&
Dom Expedito Lopes-PI&
Dom Inocêncio-PI&
Domingos Mourão-PI&
Elesbão Veloso-PI&
Eliseu Martins-PI&
Esperantina-PI&
Fartura do Piauí-PI&
Flores do Piauí-PI&
Floresta do Piauí-PI&
Floriano-PI&
Francinópolis-PI&
Francisco Ayres-PI&
Francisco Macedo-PI&
Francisco Santos-PI&
Fronteiras-PI&
Geminiano-PI&
Gilbués-PI&
Guadalupe-PI&
Guaribas-PI&
Hugo Napoleão-PI&
Ilha Grande-PI&
Inhuma-PI&
Ipiranga do Piauí-PI&
Isaías Coelho-PI&
Itainópolis-PI&
Itaueira-PI&
Jacobina do Piauí-PI&
Jaicós-PI&
Jardim do Mulato-PI&
Jatobá do Piauí-PI&
Jerumenha-PI&
João Costa-PI&
Joaquim Pires-PI&
Joca Marques-PI&
José de Freitas-PI&
Juazeiro do Piauí-PI&
Júlio Borges-PI&
Jurema-PI&
Lagoa Alegre-PI&
Lagoa de São Francisco-PI&
Lagoa do Barro do Piauí-PI&
Lagoa do Piauí-PI&
Lagoa do Sítio-PI&
Lagoinha do Piauí-PI&
Landri Sales-PI&
Luís Correia-PI&
Luzilândia-PI&
Madeiro-PI&
Manoel Emídio-PI&
Marcolândia-PI&
Marcos Parente-PI&
Massapê do Piauí-PI&
Matias Olímpio-PI&
Miguel Alves-PI&
Miguel Leão-PI&
Milton Brandão-PI&
Monsenhor Gil-PI&
Monsenhor Hipólito-PI&
Monte Alegre do Piauí-PI&
Morro Cabeça no Tempo-PI&
Morro do Chapéu do Piauí-PI&
Murici dos Portelas-PI&
Nazaré do Piauí-PI&
Nossa Senhora de Nazaré-PI&
Nossa Senhora dos Remédios-PI&
Nova Santa Rita-PI&
Novo Oriente do Piauí-PI&
Novo Santo Antônio-PI&
Oeiras-PI&
Olho D'Água do Piauí-PI&
Padre Marcos-PI&
Paes Landim-PI&
Pajeú do Piauí-PI&
Palmeira do Piauí-PI&
Palmeirais-PI&
Paquetá-PI&
Parnaguá-PI&
Parnaíba-PI&
Passagem Franca do Piauí-PI&
Patos do Piauí-PI&
Pau D'Arco do Piauí-PI&
Paulistana-PI&
Pavussu-PI&
Pedro II-PI&
Pedro Laurentino-PI&
Picos-PI&
Pimenteiras-PI&
Pio IX-PI&
Piracuruca-PI&
Piripiri-PI&
Porto-PI&
Porto Alegre do Piauí-PI&
Prata do Piauí-PI&
Queimada Nova-PI&
Redenção do Gurguéia-PI&
Regeneração-PI&
Riacho Frio-PI&
Ribeira do Piauí-PI&
Ribeiro Gonçalves-PI&
Rio Grande do Piauí-PI&
Santa Cruz do Piauí-PI&
Santa Cruz dos Milagres-PI&
Santa Filomena-PI&
Santa Luz-PI&
Santa Rosa do Piauí-PI&
Santana do Piauí-PI&
Santo Antônio de Lisboa-PI&
Santo Antônio dos Milagres-PI&
Santo Inácio do Piauí-PI&
São Braz do Piauí-PI&
São Félix do Piauí-PI&
São Francisco de Assis do Piauí-PI&
São Francisco do Piauí-PI&
São Gonçalo do Gurguéia-PI&
São Gonçalo do Piauí-PI&
São João da Canabrava-PI&
São João da Fronteira-PI&
São João da Serra-PI&
São João da Varjota-PI&
São João do Arraial-PI&
São João do Piauí-PI&
São José do Divino-PI&
São José do Peixe-PI&
São José do Piauí-PI&
São Julião-PI&
São Lourenço do Piauí-PI&
São Luis do Piauí-PI&
São Miguel da Baixa Grande-PI&
São Miguel do Fidalgo-PI&
São Miguel do Tapuio-PI&
São Pedro do Piauí-PI&
São Raimundo Nonato-PI&
Sebastião Barros-PI&
Sebastião Leal-PI&
Sigefredo Pacheco-PI&
Simões-PI&
Simplício Mendes-PI&
Socorro do Piauí-PI&
Sussuapara-PI&
Tamboril do Piauí-PI&
Tanque do Piauí-PI&
Teresina-PI&
União-PI&
Uruçuí-PI&
Valença do Piauí-PI&
Várzea Branca-PI&
Várzea Grande-PI&
Vera Mendes-PI&
Vila Nova do Piauí-PI&
Wall Ferraz-PI&
Abaiara-CE&
Acarape-CE&
Acaraú-CE&
Acopiara-CE&
Aiuaba-CE&
Alcântaras-CE&
Altaneira-CE&
Alto Santo-CE&
Amontada-CE&
Antonina do Norte-CE&
Apuiarés-CE&
Aquiraz-CE&
Aracati-CE&
Aracoiaba-CE&
Ararendá-CE&
Araripe-CE&
Aratuba-CE&
Arneiroz-CE&
Assaré-CE&
Aurora-CE&
Baixio-CE&
Banabuiú-CE&
Barbalha-CE&
Barreira-CE&
Barro-CE&
Barroquinha-CE&
Baturité-CE&
Beberibe-CE&
Bela Cruz-CE&
Boa Viagem-CE&
Brejo Santo-CE&
Camocim-CE&
Campos Sales-CE&
Canindé-CE&
Capistrano-CE&
Caridade-CE&
Cariré-CE&
Caririaçu-CE&
Cariús-CE&
Carnaubal-CE&
Cascavel-CE&
Catarina-CE&
Catunda-CE&
Caucaia-CE&
Cedro-CE&
Chaval-CE&
Choró-CE&
Chorozinho-CE&
Coreaú-CE&
Crateús-CE&
Crato-CE&
Croatá-CE&
Cruz-CE&
Deputado Irapuan Pinheiro-CE&
Ererê-CE&
Eusébio-CE&
Farias Brito-CE&
Forquilha-CE&
Fortaleza-CE&
Fortim-CE&
Frecheirinha-CE&
General Sampaio-CE&
Graça-CE&
Granja-CE&
Granjeiro-CE&
Groaíras-CE&
Guaiúba-CE&
Guaraciaba do Norte-CE&
Guaramiranga-CE&
Hidrolândia-CE&
Horizonte-CE&
Ibaretama-CE&
Ibiapina-CE&
Ibicuitinga-CE&
Icapuí-CE&
Icó-CE&
Iguatu-CE&
Independência-CE&
Ipaporanga-CE&
Ipaumirim-CE&
Ipu-CE&
Ipueiras-CE&
Iracema-CE&
Irauçuba-CE&
Itaiçaba-CE&
Itaitinga-CE&
Itapagé-CE&
Itapipoca-CE&
Itapiúna-CE&
Itarema-CE&
Itatira-CE&
Jaguaretama-CE&
Jaguaribara-CE&
Jaguaribe-CE&
Jaguaruana-CE&
Jardim-CE&
Jati-CE&
Jijoca de Jericoacoara-CE&
Juazeiro do Norte-CE&
Jucás-CE&
Lavras da Mangabeira-CE&
Limoeiro do Norte-CE&
Madalena-CE&
Maracanaú-CE&
Maranguape-CE&
Marco-CE&
Martinópole-CE&
Massapê-CE&
Mauriti-CE&
Meruoca-CE&
Milagres-CE&
Milhã-CE&
Miraíma-CE&
Missão Velha-CE&
Mombaça-CE&
Monsenhor Tabosa-CE&
Morada Nova-CE&
Moraújo-CE&
Morrinhos-CE&
Mucambo-CE&
Mulungu-CE&
Nova Olinda-CE&
Nova Russas-CE&
Novo Oriente-CE&
Ocara-CE&
Orós-CE&
Pacajus-CE&
Pacatuba-CE&
Pacoti-CE&
Pacujá-CE&
Palhano-CE&
Palmácia-CE&
Paracuru-CE&
Paraipaba-CE&
Parambu-CE&
Paramoti-CE&
Pedra Branca-CE&
Penaforte-CE&
Pentecoste-CE&
Pereiro-CE&
Pindoretama-CE&
Piquet Carneiro-CE&
Pires Ferreira-CE&
Poranga-CE&
Porteiras-CE&
Potengi-CE&
Potiretama-CE&
Quiterianópolis-CE&
Quixadá-CE&
Quixelô-CE&
Quixeramobim-CE&
Quixeré-CE&
Redenção-CE&
Reriutaba-CE&
Russas-CE&
Saboeiro-CE&
Salitre-CE&
Santa Quitéria-CE&
Santana do Acaraú-CE&
Santana do Cariri-CE&
São Benedito-CE&
São Gonçalo do Amarante-CE&
São João do Jaguaribe-CE&
São Luís do Curu-CE&
Senador Pompeu-CE&
Senador Sá-CE&
Sobral-CE&
Solonópole-CE&
Tabuleiro do Norte-CE&
Tamboril-CE&
Tarrafas-CE&
Tauá-CE&
Tejuçuoca-CE&
Tianguá-CE&
Trairi-CE&
Tururu-CE&
Ubajara-CE&
Umari-CE&
Umirim-CE&
Uruburetama-CE&
Uruoca-CE&
Varjota-CE&
Várzea Alegre-CE&
Viçosa do Ceará-CE&
Acari-RN&
Açu-RN&
Afonso Bezerra-RN&
Água Nova-RN&
Alexandria-RN&
Almino Afonso-RN&
Alto do Rodrigues-RN&
Angicos-RN&
Antônio Martins-RN&
Apodi-RN&
Areia Branca-RN&
Arês-RN&
Augusto Severo-RN&
Baía Formosa-RN&
Baraúna-RN&
Barcelona-RN&
Bento Fernandes-RN&
Bodó-RN&
Bom Jesus-RN&
Brejinho-RN&
Caiçara do Norte-RN&
Caiçara do Rio do Vento-RN&
Caicó-RN&
Campo Redondo-RN&
Canguaretama-RN&
Caraúbas-RN&
Carnaúba dos Dantas-RN&
Carnaubais-RN&
Ceará-Mirim-RN&
Cerro Corá-RN&
Coronel Ezequiel-RN&
Coronel João Pessoa-RN&
Cruzeta-RN&
Currais Novos-RN&
Doutor Severiano-RN&
Encanto-RN&
Equador-RN&
Espírito Santo-RN&
Extremoz-RN&
Felipe Guerra-RN&
Fernando Pedroza-RN&
Florânia-RN&
Francisco Dantas-RN&
Frutuoso Gomes-RN&
Galinhos-RN&
Goianinha-RN&
Governador Dix-Sept Rosado-RN&
Grossos-RN&
Guamaré-RN&
Ielmo Marinho-RN&
Ipanguaçu-RN&
Ipueira-RN&
Itajá-RN&
Itaú-RN&
Jaçanã-RN&
Jandaíra-RN&
Janduís-RN&
Januário Cicco-RN&
Japi-RN&
Jardim de Angicos-RN&
Jardim de Piranhas-RN&
Jardim do Seridó-RN&
João Câmara-RN&
João Dias-RN&
José da Penha-RN&
Jucurutu-RN&
Jundiá-RN&
Lagoa d'Anta-RN&
Lagoa de Pedras-RN&
Lagoa de Velhos-RN&
Lagoa Nova-RN&
Lagoa Salgada-RN&
Lajes-RN&
Lajes Pintadas-RN&
Lucrécia-RN&
Luís Gomes-RN&
Macaíba-RN&
Macau-RN&
Major Sales-RN&
Marcelino Vieira-RN&
Martins-RN&
Maxaranguape-RN&
Messias Targino-RN&
Montanhas-RN&
Monte Alegre-RN&
Monte das Gameleiras-RN&
Mossoró-RN&
Natal-RN&
Nísia Floresta-RN&
Nova Cruz-RN&
Olho-d'Água do Borges-RN&
Ouro Branco-RN&
Paraná-RN&
Paraú-RN&
Parazinho-RN&
Parelhas-RN&
Parnamirim-RN&
Passa e Fica-RN&
Passagem-RN&
Patu-RN&
Pau dos Ferros-RN&
Pedra Grande-RN&
Pedra Preta-RN&
Pedro Avelino-RN&
Pedro Velho-RN&
Pendências-RN&
Pilões-RN&
Poço Branco-RN&
Portalegre-RN&
Porto do Mangue-RN&
Presidente Juscelino-RN&
Pureza-RN&
Rafael Fernandes-RN&
Rafael Godeiro-RN&
Riacho da Cruz-RN&
Riacho de Santana-RN&
Riachuelo-RN&
Rio do Fogo-RN&
Rodolfo Fernandes-RN&
Ruy Barbosa-RN&
Santa Cruz-RN&
Santa Maria-RN&
Santana do Matos-RN&
Santana do Seridó-RN&
Santo Antônio-RN&
São Bento do Norte-RN&
São Bento do Trairí-RN&
São Fernando-RN&
São Francisco do Oeste-RN&
São Gonçalo do Amarante-RN&
São João do Sabugi-RN&
São José de Mipibu-RN&
São José do Campestre-RN&
São José do Seridó-RN&
São Miguel-RN&
São Miguel do Gostoso-RN&
São Paulo do Potengi-RN&
São Pedro-RN&
São Rafael-RN&
São Tomé-RN&
São Vicente-RN&
Senador Elói de Souza-RN&
Senador Georgino Avelino-RN&
Serra de São Bento-RN&
Serra do Mel-RN&
Serra Negra do Norte-RN&
Serrinha-RN&
Serrinha dos Pintos-RN&
Severiano Melo-RN&
Sítio Novo-RN&
Taboleiro Grande-RN&
Taipu-RN&
Tangará-RN&
Tenente Ananias-RN&
Tenente Laurentino Cruz-RN&
Tibau-RN&
Tibau do Sul-RN&
Timbaúba dos Batistas-RN&
Touros-RN&
Triunfo Potiguar-RN&
Umarizal-RN&
Upanema-RN&
Várzea-RN&
Venha-Ver-RN&
Vera Cruz-RN&
Viçosa-RN&
Vila Flor-RN&
Água Branca-PB&
Aguiar-PB&
Alagoa Grande-PB&
Alagoa Nova-PB&
Alagoinha-PB&
Alcantil-PB&
Algodão de Jandaíra-PB&
Alhandra-PB&
Amparo-PB&
Aparecida-PB&
Araçagi-PB&
Arara-PB&
Araruna-PB&
Areia-PB&
Areia de Baraúnas-PB&
Areial-PB&
Aroeiras-PB&
Assunção-PB&
Baía da Traição-PB&
Bananeiras-PB&
Baraúna-PB&
Barra de Santa Rosa-PB&
Barra de Santana-PB&
Barra de São Miguel-PB&
Bayeux-PB&
Belém-PB&
Belém do Brejo do Cruz-PB&
Bernardino Batista-PB&
Boa Ventura-PB&
Boa Vista-PB&
Bom Jesus-PB&
Bom Sucesso-PB&
Bonito de Santa Fé-PB&
Boqueirão-PB&
Borborema-PB&
Brejo do Cruz-PB&
Brejo dos Santos-PB&
Caaporã-PB&
Cabaceiras-PB&
Cabedelo-PB&
Cachoeira dos Índios-PB&
Cacimba de Areia-PB&
Cacimba de Dentro-PB&
Cacimbas-PB&
Caiçara-PB&
Cajazeiras-PB&
Cajazeirinhas-PB&
Caldas Brandão-PB&
Camalaú-PB&
Campina Grande-PB&
Campo de Santana-PB&
Capim-PB&
Caraúbas-PB&
Carrapateira-PB&
Casserengue-PB&
Catingueira-PB&
Catolé do Rocha-PB&
Caturité-PB&
Conceição-PB&
Condado-PB&
Conde-PB&
Congo-PB&
Coremas-PB&
Coxixola-PB&
Cruz do Espírito Santo-PB&
Cubati-PB&
Cuité-PB&
Cuité de Mamanguape-PB&
Cuitegi-PB&
Curral de Cima-PB&
Curral Velho-PB&
Damião-PB&
Desterro-PB&
Diamante-PB&
Dona Inês-PB&
Duas Estradas-PB&
Emas-PB&
Esperança-PB&
Fagundes-PB&
Frei Martinho-PB&
Gado Bravo-PB&
Guarabira-PB&
Gurinhém-PB&
Gurjão-PB&
Ibiara-PB&
Igaracy-PB&
Imaculada-PB&
Ingá-PB&
Itabaiana-PB&
Itaporanga-PB&
Itapororoca-PB&
Itatuba-PB&
Jacaraú-PB&
Jericó-PB&
João Pessoa-PB&
Juarez Távora-PB&
Juazeirinho-PB&
Junco do Seridó-PB&
Juripiranga-PB&
Juru-PB&
Lagoa-PB&
Lagoa de Dentro-PB&
Lagoa Seca-PB&
Lastro-PB&
Livramento-PB&
Logradouro-PB&
Lucena-PB&
Mãe d'Água-PB&
Malta-PB&
Mamanguape-PB&
Manaíra-PB&
Marcação-PB&
Mari-PB&
Marizópolis-PB&
Massaranduba-PB&
Mataraca-PB&
Matinhas-PB&
Mato Grosso-PB&
Maturéia-PB&
Mogeiro-PB&
Montadas-PB&
Monte Horebe-PB&
Monteiro-PB&
Mulungu-PB&
Natuba-PB&
Nazarezinho-PB&
Nova Floresta-PB&
Nova Olinda-PB&
Nova Palmeira-PB&
Olho d'Água-PB&
Olivedos-PB&
Ouro Velho-PB&
Parari-PB&
Passagem-PB&
Patos-PB&
Paulista-PB&
Pedra Branca-PB&
Pedra Lavrada-PB&
Pedras de Fogo-PB&
Pedro Régis-PB&
Piancó-PB&
Picuí-PB&
Pilar-PB&
Pilões-PB&
Pilõezinhos-PB&
Pirpirituba-PB&
Pitimbu-PB&
Pocinhos-PB&
Poço Dantas-PB&
Poço de José de Moura-PB&
Pombal-PB&
Prata-PB&
Princesa Isabel-PB&
Puxinanã-PB&
Queimadas-PB&
Quixabá-PB&
Remígio-PB&
Riachão-PB&
Riachão do Bacamarte-PB&
Riachão do Poço-PB&
Riacho de Santo Antônio-PB&
Riacho dos Cavalos-PB&
Rio Tinto-PB&
Salgadinho-PB&
Salgado de São Félix-PB&
Santa Cecília-PB&
Santa Cruz-PB&
Santa Helena-PB&
Santa Inês-PB&
Santa Luzia-PB&
Santa Rita-PB&
Santa Teresinha-PB&
Santana de Mangueira-PB&
Santana dos Garrotes-PB&
Santarém-PB&
Santo André-PB&
São Bentinho-PB&
São Bento-PB&
São Domingos de Pombal-PB&
São Domingos do Cariri-PB&
São Francisco-PB&
São João do Cariri-PB&
São João do Rio do Peixe-PB&
São João do Tigre-PB&
São José da Lagoa Tapada-PB&
São José de Caiana-PB&
São José de Espinharas-PB&
São José de Piranhas-PB&
São José de Princesa-PB&
São José do Bonfim-PB&
São José do Brejo do Cruz-PB&
São José do Sabugi-PB&
São José dos Cordeiros-PB&
São José dos Ramos-PB&
São Mamede-PB&
São Miguel de Taipu-PB&
São Sebastião de Lagoa de Roça-PB&
São Sebastião do Umbuzeiro-PB&
Sapé-PB&
Seridó-PB&
Serra Branca-PB&
Serra da Raiz-PB&
Serra Grande-PB&
Serra Redonda-PB&
Serraria-PB&
Sertãozinho-PB&
Sobrado-PB&
Solânea-PB&
Soledade-PB&
Sossêgo-PB&
Sousa-PB&
Sumé-PB&
Taperoá-PB&
Tavares-PB&
Teixeira-PB&
Tenório-PB&
Triunfo-PB&
Uiraúna-PB&
Umbuzeiro-PB&
Várzea-PB&
Vieirópolis-PB&
Vista Serrana-PB&
Zabelê-PB&
Abreu e Lima-PE&
Afogados da Ingazeira-PE&
Afrânio-PE&
Agrestina-PE&
Água Preta-PE&
Águas Belas-PE&
Alagoinha-PE&
Aliança-PE&
Altinho-PE&
Amaraji-PE&
Angelim-PE&
Araçoiaba-PE&
Araripina-PE&
Arcoverde-PE&
Barra de Guabiraba-PE&
Barreiros-PE&
Belém de Maria-PE&
Belém de São Francisco-PE&
Belo Jardim-PE&
Betânia-PE&
Bezerros-PE&
Bodocó-PE&
Bom Conselho-PE&
Bom Jardim-PE&
Bonito-PE&
Brejão-PE&
Brejinho-PE&
Brejo da Madre de Deus-PE&
Buenos Aires-PE&
Buíque-PE&
Cabo de Santo Agostinho-PE&
Cabrobó-PE&
Cachoeirinha-PE&
Caetés-PE&
Calçado-PE&
Calumbi-PE&
Camaragibe-PE&
Camocim de São Félix-PE&
Camutanga-PE&
Canhotinho-PE&
Capoeiras-PE&
Carnaíba-PE&
Carnaubeira da Penha-PE&
Carpina-PE&
Caruaru-PE&
Casinhas-PE&
Catende-PE&
Cedro-PE&
Chã de Alegria-PE&
Chã Grande-PE&
Condado-PE&
Correntes-PE&
Cortês-PE&
Cumaru-PE&
Cupira-PE&
Custódia-PE&
Dormentes-PE&
Escada-PE&
Exu-PE&
Feira Nova-PE&
Fernando de Noronha-PE&
Ferreiros-PE&
Flores-PE&
Floresta-PE&
Frei Miguelinho-PE&
Gameleira-PE&
Garanhuns-PE&
Glória do Goitá-PE&
Goiana-PE&
Granito-PE&
Gravatá-PE&
Iati-PE&
Ibimirim-PE&
Ibirajuba-PE&
Igarassu-PE&
Iguaraci-PE&
Ilha de Itamaracá-PE&
Inajá-PE&
Ingazeira-PE&
Ipojuca-PE&
Ipubi-PE&
Itacuruba-PE&
Itaíba-PE&
Itambé-PE&
Itapetim-PE&
Itapissuma-PE&
Itaquitinga-PE&
Jaboatão dos Guararapes-PE&
Jaqueira-PE&
Jataúba-PE&
Jatobá-PE&
João Alfredo-PE&
Joaquim Nabuco-PE&
Jucati-PE&
Jupi-PE&
Jurema-PE&
Lagoa do Carro-PE&
Lagoa do Itaenga-PE&
Lagoa do Ouro-PE&
Lagoa dos Gatos-PE&
Lagoa Grande-PE&
Lajedo-PE&
Limoeiro-PE&
Macaparana-PE&
Machados-PE&
Manari-PE&
Maraial-PE&
Mirandiba-PE&
Moreilândia-PE&
Moreno-PE&
Nazaré da Mata-PE&
Olinda-PE&
Orobó-PE&
Orocó-PE&
Ouricuri-PE&
Palmares-PE&
Palmeirina-PE&
Panelas-PE&
Paranatama-PE&
Parnamirim-PE&
Passira-PE&
Paudalho-PE&
Paulista-PE&
Pedra-PE&
Pesqueira-PE&
Petrolândia-PE&
Petrolina-PE&
Poção-PE&
Pombos-PE&
Primavera-PE&
Quipapá-PE&
Quixaba-PE&
Recife-PE&
Riacho das Almas-PE&
Ribeirão-PE&
Rio Formoso-PE&
Sairé-PE&
Salgadinho-PE&
Salgueiro-PE&
Saloá-PE&
Sanharó-PE&
Santa Cruz-PE&
Santa Cruz da Baixa Verde-PE&
Santa Cruz do Capibaribe-PE&
Santa Filomena-PE&
Santa Maria da Boa Vista-PE&
Santa Maria do Cambucá-PE&
Santa Terezinha-PE&
São Benedito do Sul-PE&
São Bento do Una-PE&
São Caitano-PE&
São João-PE&
São Joaquim do Monte-PE&
São José da Coroa Grande-PE&
São José do Belmonte-PE&
São José do Egito-PE&
São Lourenço da Mata-PE&
São Vicente Ferrer-PE&
Serra Talhada-PE&
Serrita-PE&
Sertânia-PE&
Sirinhaém-PE&
Solidão-PE&
Surubim-PE&
Tabira-PE&
Tacaimbó-PE&
Tacaratu-PE&
Tamandaré-PE&
Taquaritinga do Norte-PE&
Terezinha-PE&
Terra Nova-PE&
Timbaúba-PE&
Toritama-PE&
Tracunhaém-PE&
Trindade-PE&
Triunfo-PE&
Tupanatinga-PE&
Tuparetama-PE&
Venturosa-PE&
Verdejante-PE&
Vertente do Lério-PE&
Vertentes-PE&
Vicência-PE&
Vitória de Santo Antão-PE&
Xexéu-PE&
Água Branca-AL&
Anadia-AL&
Arapiraca-AL&
Atalaia-AL&
Barra de Santo Antônio-AL&
Barra de São Miguel-AL&
Batalha-AL&
Belém-AL&
Belo Monte-AL&
Boca da Mata-AL&
Branquinha-AL&
Cacimbinhas-AL&
Cajueiro-AL&
Campestre-AL&
Campo Alegre-AL&
Campo Grande-AL&
Canapi-AL&
Capela-AL&
Carneiros-AL&
Chã Preta-AL&
Coité do Nóia-AL&
Colônia Leopoldina-AL&
Coqueiro Seco-AL&
Coruripe-AL&
Craíbas-AL&
Delmiro Gouveia-AL&
Dois Riachos-AL&
Estrela de Alagoas-AL&
Feira Grande-AL&
Feliz Deserto-AL&
Flexeiras-AL&
Girau do Ponciano-AL&
Ibateguara-AL&
Igaci-AL&
Igreja Nova-AL&
Inhapi-AL&
Jacaré dos Homens-AL&
Jacuípe-AL&
Japaratinga-AL&
Jaramataia-AL&
Jequiá da Praia-AL&
Joaquim Gomes-AL&
Jundiá-AL&
Junqueiro-AL&
Lagoa da Canoa-AL&
Limoeiro de Anadia-AL&
Maceió-AL&
Major Isidoro-AL&
Mar Vermelho-AL&
Maragogi-AL&
Maravilha-AL&
Marechal Deodoro-AL&
Maribondo-AL&
Mata Grande-AL&
Matriz de Camaragibe-AL&
Messias-AL&
Minador do Negrão-AL&
Monteirópolis-AL&
Murici-AL&
Novo Lino-AL&
Olho d'Água das Flores-AL&
Olho d'Água do Casado-AL&
Olho d'Água Grande-AL&
Olivença-AL&
Ouro Branco-AL&
Palestina-AL&
Palmeira dos Índios-AL&
Pão de Açúcar-AL&
Pariconha-AL&
Paripueira-AL&
Passo de Camaragibe-AL&
Paulo Jacinto-AL&
Penedo-AL&
Piaçabuçu-AL&
Pilar-AL&
Pindoba-AL&
Piranhas-AL&
Poço das Trincheiras-AL&
Porto Calvo-AL&
Porto de Pedras-AL&
Porto Real do Colégio-AL&
Quebrangulo-AL&
Rio Largo-AL&
Roteiro-AL&
Santa Luzia do Norte-AL&
Santana do Ipanema-AL&
Santana do Mundaú-AL&
São Brás-AL&
São José da Laje-AL&
São José da Tapera-AL&
São Luís do Quitunde-AL&
São Miguel dos Campos-AL&
São Miguel dos Milagres-AL&
São Sebastião-AL&
Satuba-AL&
Senador Rui Palmeira-AL&
Tanque d'Arca-AL&
Taquarana-AL&
Teotônio Vilela-AL&
Traipu-AL&
União dos Palmares-AL&
Viçosa-AL&
Amparo de São Francisco-SE&
Aquidabã-SE&
Aracaju-SE&
Arauá-SE&
Areia Branca-SE&
Barra dos Coqueiros-SE&
Boquim-SE&
Brejo Grande-SE&
Campo do Brito-SE&
Canhoba-SE&
Canindé de São Francisco-SE&
Capela-SE&
Carira-SE&
Carmópolis-SE&
Cedro de São João-SE&
Cristinápolis-SE&
Cumbe-SE&
Divina Pastora-SE&
Estância-SE&
Feira Nova-SE&
Frei Paulo-SE&
Gararu-SE&
General Maynard-SE&
Gracho Cardoso-SE&
Ilha das Flores-SE&
Indiaroba-SE&
Itabaiana-SE&
Itabaianinha-SE&
Itabi-SE&
Itaporanga d'Ajuda-SE&
Japaratuba-SE&
Japoatã-SE&
Lagarto-SE&
Laranjeiras-SE&
Macambira-SE&
Malhada dos Bois-SE&
Malhador-SE&
Maruim-SE&
Moita Bonita-SE&
Monte Alegre de Sergipe-SE&
Muribeca-SE&
Neópolis-SE&
Nossa Senhora Aparecida-SE&
Nossa Senhora da Glória-SE&
Nossa Senhora das Dores-SE&
Nossa Senhora de Lourdes-SE&
Nossa Senhora do Socorro-SE&
Pacatuba-SE&
Pedra Mole-SE&
Pedrinhas-SE&
Pinhão-SE&
Pirambu-SE&
Poço Redondo-SE&
Poço Verde-SE&
Porto da Folha-SE&
Propriá-SE&
Riachão do Dantas-SE&
Riachuelo-SE&
Ribeirópolis-SE&
Rosário do Catete-SE&
Salgado-SE&
Santa Luzia do Itanhy-SE&
Santa Rosa de Lima-SE&
Santana do São Francisco-SE&
Santo Amaro das Brotas-SE&
São Cristóvão-SE&
São Domingos-SE&
São Francisco-SE&
São Miguel do Aleixo-SE&
Simão Dias-SE&
Siriri-SE&
Telha-SE&
Tobias Barreto-SE&
Tomar do Geru-SE&
Umbaúba-SE&
Abaíra-BA&
Abaré-BA&
Acajutiba-BA&
Adustina-BA&
Água Fria-BA&
Aiquara-BA&
Alagoinhas-BA&
Alcobaça-BA&
Almadina-BA&
Amargosa-BA&
Amélia Rodrigues-BA&
América Dourada-BA&
Anagé-BA&
Andaraí-BA&
Andorinha-BA&
Angical-BA&
Anguera-BA&
Antas-BA&
Antônio Cardoso-BA&
Antônio Gonçalves-BA&
Aporá-BA&
Apuarema-BA&
Araças-BA&
Aracatu-BA&
Araci-BA&
Aramari-BA&
Arataca-BA&
Aratuípe-BA&
Aurelino Leal-BA&
Baianópolis-BA&
Baixa Grande-BA&
Banzaê-BA&
Barra-BA&
Barra da Estiva-BA&
Barra do Choça-BA&
Barra do Mendes-BA&
Barra do Rocha-BA&
Barreiras-BA&
Barro Alto-BA&
Barro Preto-BA&
Barrocas-BA&
Belmonte-BA&
Belo Campo-BA&
Biritinga-BA&
Boa Nova-BA&
Boa Vista do Tupim-BA&
Bom Jesus da Lapa-BA&
Bom Jesus da Serra-BA&
Boninal-BA&
Bonito-BA&
Boquira-BA&
Botuporã-BA&
Brejões-BA&
Brejolândia-BA&
Brotas de Macaúbas-BA&
Brumado-BA&
Buerarema-BA&
Buritirama-BA&
Caatiba-BA&
Cabaceiras do Paraguaçu-BA&
Cachoeira-BA&
Caculé-BA&
Caém-BA&
Caetanos-BA&
Caetité-BA&
Cafarnaum-BA&
Cairu-BA&
Caldeirão Grande-BA&
Camacan-BA&
Camaçari-BA&
Camamu-BA&
Campo Alegre de Lourdes-BA&
Campo Formoso-BA&
Canápolis-BA&
Canarana-BA&
Canavieiras-BA&
Candeal-BA&
Candeias-BA&
Candiba-BA&
Cândido Sales-BA&
Cansanção-BA&
Canudos-BA&
Capela do Alto Alegre-BA&
Capim Grosso-BA&
Caraíbas-BA&
Caravelas-BA&
Cardeal da Silva-BA&
Carinhanha-BA&
Casa Nova-BA&
Castro Alves-BA&
Catolândia-BA&
Catu-BA&
Caturama-BA&
Central-BA&
Chorrochó-BA&
Cícero Dantas-BA&
Cipó-BA&
Coaraci-BA&
Cocos-BA&
Conceição da Feira-BA&
Conceição do Almeida-BA&
Conceição do Coité-BA&
Conceição do Jacuípe-BA&
Conde-BA&
Condeúba-BA&
Contendas do Sincorá-BA&
Coração de Maria-BA&
Cordeiros-BA&
Coribe-BA&
Coronel João Sá-BA&
Correntina-BA&
Cotegipe-BA&
Cravolândia-BA&
Crisópolis-BA&
Cristópolis-BA&
Cruz das Almas-BA&
Curaçá-BA&
Dário Meira-BA&
Dias d'Ávila-BA&
Dom Basílio-BA&
Dom Macedo Costa-BA&
Elísio Medrado-BA&
Encruzilhada-BA&
Entre Rios-BA&
Érico Cardoso-BA&
Esplanada-BA&
Euclides da Cunha-BA&
Eunápolis-BA&
Fátima-BA&
Feira da Mata-BA&
Feira de Santana-BA&
Filadélfia-BA&
Firmino Alves-BA&
Floresta Azul-BA&
Formosa do Rio Preto-BA&
Gandu-BA&
Gavião-BA&
Gentio do Ouro-BA&
Glória-BA&
Gongogi-BA&
Governador Mangabeira-BA&
Guajeru-BA&
Guanambi-BA&
Guaratinga-BA&
Heliópolis-BA&
Iaçu-BA&
Ibiassucê-BA&
Ibicaraí-BA&
Ibicoara-BA&
Ibicuí-BA&
Ibipeba-BA&
Ibipitanga-BA&
Ibiquera-BA&
Ibirapitanga-BA&
Ibirapuã-BA&
Ibirataia-BA&
Ibitiara-BA&
Ibititá-BA&
Ibotirama-BA&
Ichu-BA&
Igaporã-BA&
Igrapiúna-BA&
Iguaí-BA&
Ilhéus-BA&
Inhambupe-BA&
Ipecaetá-BA&
Ipiaú-BA&
Ipirá-BA&
Ipupiara-BA&
Irajuba-BA&
Iramaia-BA&
Iraquara-BA&
Irará-BA&
Irecê-BA&
Itabela-BA&
Itaberaba-BA&
Itabuna-BA&
Itacaré-BA&
Itaeté-BA&
Itagi-BA&
Itagibá-BA&
Itagimirim-BA&
Itaguaçu da Bahia-BA&
Itaju do Colônia-BA&
Itajuípe-BA&
Itamaraju-BA&
Itamari-BA&
Itambé-BA&
Itanagra-BA&
Itanhém-BA&
Itaparica-BA&
Itapé-BA&
Itapebi-BA&
Itapetinga-BA&
Itapicuru-BA&
Itapitanga-BA&
Itaquara-BA&
Itarantim-BA&
Itatim-BA&
Itiruçu-BA&
Itiúba-BA&
Itororó-BA&
Ituaçu-BA&
Ituberá-BA&
Iuiú-BA&
Jaborandi-BA&
Jacaraci-BA&
Jacobina-BA&
Jaguaquara-BA&
Jaguarari-BA&
Jaguaripe-BA&
Jandaíra-BA&
Jequié-BA&
Jeremoabo-BA&
Jiquiriçá-BA&
Jitaúna-BA&
João Dourado-BA&
Juazeiro-BA&
Jucuruçu-BA&
Jussara-BA&
Jussari-BA&
Jussiape-BA&
Lafaiete Coutinho-BA&
Lagoa Real-BA&
Laje-BA&
Lajedão-BA&
Lajedinho-BA&
Lajedo do Tabocal-BA&
Lamarão-BA&
Lapão-BA&
Lauro de Freitas-BA&
Lençóis-BA&
Licínio de Almeida-BA&
Livramento de Nossa Senhora-BA&
Luís Eduardo Magalhães-BA&
Macajuba-BA&
Macarani-BA&
Macaúbas-BA&
Macururé-BA&
Madre de Deus-BA&
Maetinga-BA&
Maiquinique-BA&
Mairi-BA&
Malhada-BA&
Malhada de Pedras-BA&
Manoel Vitorino-BA&
Mansidão-BA&
Maracás-BA&
Maragogipe-BA&
Maraú-BA&
Marcionílio Souza-BA&
Mascote-BA&
Mata de São João-BA&
Matina-BA&
Medeiros Neto-BA&
Miguel Calmon-BA&
Milagres-BA&
Mirangaba-BA&
Mirante-BA&
Monte Santo-BA&
Morpará-BA&
Morro do Chapéu-BA&
Mortugaba-BA&
Mucugê-BA&
Mucuri-BA&
Mulungu do Morro-BA&
Mundo Novo-BA&
Muniz Ferreira-BA&
Muquém de São Francisco-BA&
Muritiba-BA&
Mutuípe-BA&
Nazaré-BA&
Nilo Peçanha-BA&
Nordestina-BA&
Nova Canaã-BA&
Nova Fátima-BA&
Nova Ibiá-BA&
Nova Itarana-BA&
Nova Redenção-BA&
Nova Soure-BA&
Nova Viçosa-BA&
Novo Horizonte-BA&
Novo Triunfo-BA&
Olindina-BA&
Oliveira dos Brejinhos-BA&
Ouriçangas-BA&
Ourolândia-BA&
Palmas de Monte Alto-BA&
Palmeiras-BA&
Paramirim-BA&
Paratinga-BA&
Paripiranga-BA&
Pau Brasil-BA&
Paulo Afonso-BA&
Pé de Serra-BA&
Pedrão-BA&
Pedro Alexandre-BA&
Piatã-BA&
Pilão Arcado-BA&
Pindaí-BA&
Pindobaçu-BA&
Pintadas-BA&
Piraí do Norte-BA&
Piripá-BA&
Piritiba-BA&
Planaltino-BA&
Planalto-BA&
Poções-BA&
Pojuca-BA&
Ponto Novo-BA&
Porto Seguro-BA&
Potiraguá-BA&
Prado-BA&
Presidente Dutra-BA&
Presidente Jânio Quadros-BA&
Presidente Tancredo Neves-BA&
Queimadas-BA&
Quijingue-BA&
Quixabeira-BA&
Rafael Jambeiro-BA&
Remanso-BA&
Retirolândia-BA&
Riachão das Neves-BA&
Riachão do Jacuípe-BA&
Riacho de Santana-BA&
Ribeira do Amparo-BA&
Ribeira do Pombal-BA&
Ribeirão do Largo-BA&
Rio de Contas-BA&
Rio do Antônio-BA&
Rio do Pires-BA&
Rio Real-BA&
Rodelas-BA&
Ruy Barbosa-BA&
Salinas da Margarida-BA&
Salvador-BA&
Santa Bárbara-BA&
Santa Brígida-BA&
Santa Cruz Cabrália-BA&
Santa Cruz da Vitória-BA&
Santa Inês-BA&
Santa Luzia-BA&
Santa Maria da Vitória-BA&
Santa Rita de Cássia-BA&
Santa Teresinha-BA&
Santaluz-BA&
Santana-BA&
Santanópolis-BA&
Santo Amaro-BA&
Santo Antônio de Jesus-BA&
Santo Estêvão-BA&
São Desidério-BA&
São Domingos-BA&
São Felipe-BA&
São Félix-BA&
São Félix do Coribe-BA&
São Francisco do Conde-BA&
São Gabriel-BA&
São Gonçalo dos Campos-BA&
São José da Vitória-BA&
São José do Jacuípe-BA&
São Miguel das Matas-BA&
São Sebastião do Passé-BA&
Sapeaçu-BA&
Sátiro Dias-BA&
Saubara-BA&
Saúde-BA&
Seabra-BA&
Sebastião Laranjeiras-BA&
Senhor do Bonfim-BA&
Sento Sé-BA&
Serra do Ramalho-BA&
Serra Dourada-BA&
Serra Preta-BA&
Serrinha-BA&
Serrolândia-BA&
Simões Filho-BA&
Sítio do Mato-BA&
Sítio do Quinto-BA&
Sobradinho-BA&
Souto Soares-BA&
Tabocas do Brejo Velho-BA&
Tanhaçu-BA&
Tanque Novo-BA&
Tanquinho-BA&
Taperoá-BA&
Tapiramutá-BA&
Teixeira de Freitas-BA&
Teodoro Sampaio-BA&
Teofilândia-BA&
Teolândia-BA&
Terra Nova-BA&
Tremedal-BA&
Tucano-BA&
Uauá-BA&
Ubaíra-BA&
Ubaitaba-BA&
Ubatã-BA&
Uibaí-BA&
Umburanas-BA&
Una-BA&
Urandi-BA&
Uruçuca-BA&
Utinga-BA&
Valença-BA&
Valente-BA&
Várzea da Roça-BA&
Várzea do Poço-BA&
Várzea Nova-BA&
Varzedo-BA&
Vera Cruz-BA&
Vereda-BA&
Vitória da Conquista-BA&
Wagner-BA&
Wanderley-BA&
Wenceslau Guimarães-BA&
Xique-Xique-BA&
Abadia dos Dourados-MG&
Abaeté-MG&
Abre Campo-MG&
Acaiaca-MG&
Açucena-MG&
Água Boa-MG&
Água Comprida-MG&
Aguanil-MG&
Águas Formosas-MG&
Águas Vermelhas-MG&
Aimorés-MG&
Aiuruoca-MG&
Alagoa-MG&
Albertina-MG&
Além Paraíba-MG&
Alfenas-MG&
Alfredo Vasconcelos-MG&
Almenara-MG&
Alpercata-MG&
Alpinópolis-MG&
Alterosa-MG&
Alto Caparaó-MG&
Alto Jequitibá-MG&
Alto Rio Doce-MG&
Alvarenga-MG&
Alvinópolis-MG&
Alvorada de Minas-MG&
Amparo do Serra-MG&
Andradas-MG&
Andrelândia-MG&
Angelândia-MG&
Antônio Carlos-MG&
Antônio Dias-MG&
Antônio Prado de Minas-MG&
Araçaí-MG&
Aracitaba-MG&
Araçuaí-MG&
Araguari-MG&
Arantina-MG&
Araponga-MG&
Araporã-MG&
Arapuá-MG&
Araújos-MG&
Araxá-MG&
Arceburgo-MG&
Arcos-MG&
Areado-MG&
Argirita-MG&
Aricanduva-MG&
Arinos-MG&
Astolfo Dutra-MG&
Ataléia-MG&
Augusto de Lima-MG&
Baependi-MG&
Baldim-MG&
Bambuí-MG&
Bandeira-MG&
Bandeira do Sul-MG&
Barão de Cocais-MG&
Barão de Monte Alto-MG&
Barbacena-MG&
Barra Longa-MG&
Barroso-MG&
Bela Vista de Minas-MG&
Belmiro Braga-MG&
Belo Horizonte-MG&
Belo Oriente-MG&
Belo Vale-MG&
Berilo-MG&
Berizal-MG&
Bertópolis-MG&
Betim-MG&
Bias Fortes-MG&
Bicas-MG&
Biquinhas-MG&
Boa Esperança-MG&
Bocaina de Minas-MG&
Bocaiúva-MG&
Bom Despacho-MG&
Bom Jardim de Minas-MG&
Bom Jesus da Penha-MG&
Bom Jesus do Amparo-MG&
Bom Jesus do Galho-MG&
Bom Repouso-MG&
Bom Sucesso-MG&
Bonfim-MG&
Bonfinópolis de Minas-MG&
Bonito de Minas-MG&
Borda da Mata-MG&
Botelhos-MG&
Botumirim-MG&
Brás Pires-MG&
Brasilândia de Minas-MG&
Brasília de Minas-MG&
Brasópolis-MG&
Braúnas-MG&
Brumadinho-MG&
Bueno Brandão-MG&
Buenópolis-MG&
Bugre-MG&
Buritis-MG&
Buritizeiro-MG&
Cabeceira Grande-MG&
Cabo Verde-MG&
Cachoeira da Prata-MG&
Cachoeira de Minas-MG&
Cachoeira de Pajeú-MG&
Cachoeira Dourada-MG&
Caetanópolis-MG&
Caeté-MG&
Caiana-MG&
Cajuri-MG&
Caldas-MG&
Camacho-MG&
Camanducaia-MG&
Cambuí-MG&
Cambuquira-MG&
Campanário-MG&
Campanha-MG&
Campestre-MG&
Campina Verde-MG&
Campo Azul-MG&
Campo Belo-MG&
Campo do Meio-MG&
Campo Florido-MG&
Campos Altos-MG&
Campos Gerais-MG&
Cana Verde-MG&
Canaã-MG&
Canápolis-MG&
Candeias-MG&
Cantagalo-MG&
Caparaó-MG&
Capela Nova-MG&
Capelinha-MG&
Capetinga-MG&
Capim Branco-MG&
Capinópolis-MG&
Capitão Andrade-MG&
Capitão Enéas-MG&
Capitólio-MG&
Caputira-MG&
Caraí-MG&
Caranaíba-MG&
Carandaí-MG&
Carangola-MG&
Caratinga-MG&
Carbonita-MG&
Careaçu-MG&
Carlos Chagas-MG&
Carmésia-MG&
Carmo da Cachoeira-MG&
Carmo da Mata-MG&
Carmo de Minas-MG&
Carmo do Cajuru-MG&
Carmo do Paranaíba-MG&
Carmo do Rio Claro-MG&
Carmópolis de Minas-MG&
Carneirinho-MG&
Carrancas-MG&
Carvalhópolis-MG&
Carvalhos-MG&
Casa Grande-MG&
Cascalho Rico-MG&
Cássia-MG&
Cataguases-MG&
Catas Altas-MG&
Catas Altas da Noruega-MG&
Catuji-MG&
Catuti-MG&
Caxambu-MG&
Cedro do Abaeté-MG&
Central de Minas-MG&
Centralina-MG&
Chácara-MG&
Chalé-MG&
Chapada do Norte-MG&
Chapada Gaúcha-MG&
Chiador-MG&
Cipotânea-MG&
Claraval-MG&
Claro dos Poções-MG&
Cláudio-MG&
Coimbra-MG&
Coluna-MG&
Comendador Gomes-MG&
Comercinho-MG&
Conceição da Aparecida-MG&
Conceição da Barra de Minas-MG&
Conceição das Alagoas-MG&
Conceição das Pedras-MG&
Conceição de Ipanema-MG&
Conceição do Mato Dentro-MG&
Conceição do Pará-MG&
Conceição do Rio Verde-MG&
Conceição dos Ouros-MG&
Cônego Marinho-MG&
Confins-MG&
Congonhal-MG&
Congonhas-MG&
Congonhas do Norte-MG&
Conquista-MG&
Conselheiro Lafaiete-MG&
Conselheiro Pena-MG&
Consolação-MG&
Contagem-MG&
Coqueiral-MG&
Coração de Jesus-MG&
Cordisburgo-MG&
Cordislândia-MG&
Corinto-MG&
Coroaci-MG&
Coromandel-MG&
Coronel Fabriciano-MG&
Coronel Murta-MG&
Coronel Pacheco-MG&
Coronel Xavier Chaves-MG&
Córrego Danta-MG&
Córrego do Bom Jesus-MG&
Córrego Fundo-MG&
Córrego Novo-MG&
Couto de Magalhães de Minas-MG&
Crisólita-MG&
Cristais-MG&
Cristália-MG&
Cristiano Otoni-MG&
Cristina-MG&
Crucilândia-MG&
Cruzeiro da Fortaleza-MG&
Cruzília-MG&
Cuparaque-MG&
Curral de Dentro-MG&
Curvelo-MG&
Datas-MG&
Delfim Moreira-MG&
Delfinópolis-MG&
Delta-MG&
Descoberto-MG&
Desterro de Entre Rios-MG&
Desterro do Melo-MG&
Diamantina-MG&
Diogo de Vasconcelos-MG&
Dionísio-MG&
Divinésia-MG&
Divino-MG&
Divino das Laranjeiras-MG&
Divinolândia de Minas-MG&
Divinópolis-MG&
Divisa Alegre-MG&
Divisa Nova-MG&
Divisópolis-MG&
Dom Bosco-MG&
Dom Cavati-MG&
Dom Joaquim-MG&
Dom Silvério-MG&
Dom Viçoso-MG&
Dona Eusébia-MG&
Dores de Campos-MG&
Dores de Guanhães-MG&
Dores do Indaiá-MG&
Dores do Turvo-MG&
Doresópolis-MG&
Douradoquara-MG&
Durandé-MG&
Elói Mendes-MG&
Engenheiro Caldas-MG&
Engenheiro Navarro-MG&
Entre Folhas-MG&
Entre Rios de Minas-MG&
Ervália-MG&
Esmeraldas-MG&
Espera Feliz-MG&
Espinosa-MG&
Espírito Santo do Dourado-MG&
Estiva-MG&
Estrela Dalva-MG&
Estrela do Indaiá-MG&
Estrela do Sul-MG&
Eugenópolis-MG&
Ewbank da Câmara-MG&
Extrema-MG&
Fama-MG&
Faria Lemos-MG&
Felício dos Santos-MG&
Felisburgo-MG&
Felixlândia-MG&
Fernandes Tourinho-MG&
Ferros-MG&
Fervedouro-MG&
Florestal-MG&
Formiga-MG&
Formoso-MG&
Fortaleza de Minas-MG&
Fortuna de Minas-MG&
Francisco Badaró-MG&
Francisco Dumont-MG&
Francisco Sá-MG&
Franciscópolis-MG&
Frei Gaspar-MG&
Frei Inocêncio-MG&
Frei Lagonegro-MG&
Fronteira-MG&
Fronteira dos Vales-MG&
Fruta de Leite-MG&
Frutal-MG&
Funilândia-MG&
Galiléia-MG&
Gameleiras-MG&
Glaucilândia-MG&
Goiabeira-MG&
Goianá-MG&
Gonçalves-MG&
Gonzaga-MG&
Gouveia-MG&
Governador Valadares-MG&
Grão Mogol-MG&
Grupiara-MG&
Guanhães-MG&
Guapé-MG&
Guaraciaba-MG&
Guaraciama-MG&
Guaranésia-MG&
Guarani-MG&
Guarará-MG&
Guarda-Mor-MG&
Guaxupé-MG&
Guidoval-MG&
Guimarânia-MG&
Guiricema-MG&
Gurinhatã-MG&
Heliodora-MG&
Iapu-MG&
Ibertioga-MG&
Ibiá-MG&
Ibiaí-MG&
Ibiracatu-MG&
Ibiraci-MG&
Ibirité-MG&
Ibitiúra de Minas-MG&
Ibituruna-MG&
Icaraí de Minas-MG&
Igarapé-MG&
Igaratinga-MG&
Iguatama-MG&
Ijaci-MG&
Ilicínea-MG&
Imbé de Minas-MG&
Inconfidentes-MG&
Indaiabira-MG&
Indianópolis-MG&
Ingaí-MG&
Inhapim-MG&
Inhaúma-MG&
Inimutaba-MG&
Ipaba-MG&
Ipanema-MG&
Ipatinga-MG&
Ipiaçu-MG&
Ipuiúna-MG&
Iraí de Minas-MG&
Itabira-MG&
Itabirinha-MG&
Itabirito-MG&
Itacambira-MG&
Itacarambi-MG&
Itaguara-MG&
Itaipé-MG&
Itajubá-MG&
Itamarandiba-MG&
Itamarati de Minas-MG&
Itambacuri-MG&
Itambé do Mato Dentro-MG&
Itamogi-MG&
Itamonte-MG&
Itanhandu-MG&
Itanhomi-MG&
Itaobim-MG&
Itapagipe-MG&
Itapecerica-MG&
Itapeva-MG&
Itatiaiuçu-MG&
Itaú de Minas-MG&
Itaúna-MG&
Itaverava-MG&
Itinga-MG&
Itueta-MG&
Ituiutaba-MG&
Itumirim-MG&
Iturama-MG&
Itutinga-MG&
Jaboticatubas-MG&
Jacinto-MG&
Jacuí-MG&
Jacutinga-MG&
Jaguaraçu-MG&
Jaíba-MG&
Jampruca-MG&
Janaúba-MG&
Januária-MG&
Japaraíba-MG&
Japonvar-MG&
Jeceaba-MG&
Jenipapo de Minas-MG&
Jequeri-MG&
Jequitaí-MG&
Jequitibá-MG&
Jequitinhonha-MG&
Jesuânia-MG&
Joaíma-MG&
Joanésia-MG&
João Monlevade-MG&
João Pinheiro-MG&
Joaquim Felício-MG&
Jordânia-MG&
José Gonçalves de Minas-MG&
José Raydan-MG&
Josenópolis-MG&
Juatuba-MG&
Juiz de Fora-MG&
Juramento-MG&
Juruaia-MG&
Juvenília-MG&
Ladainha-MG&
Lagamar-MG&
Lagoa da Prata-MG&
Lagoa dos Patos-MG&
Lagoa Dourada-MG&
Lagoa Formosa-MG&
Lagoa Grande-MG&
Lagoa Santa-MG&
Lajinha-MG&
Lambari-MG&
Lamim-MG&
Laranjal-MG&
Lassance-MG&
Lavras-MG&
Leandro Ferreira-MG&
Leme do Prado-MG&
Leopoldina-MG&
Liberdade-MG&
Lima Duarte-MG&
Limeira do Oeste-MG&
Lontra-MG&
Luisburgo-MG&
Luislândia-MG&
Luminárias-MG&
Luz-MG&
Machacalis-MG&
Machado-MG&
Madre de Deus de Minas-MG&
Malacacheta-MG&
Mamonas-MG&
Manga-MG&
Manhuaçu-MG&
Manhumirim-MG&
Mantena-MG&
Mar de Espanha-MG&
Maravilhas-MG&
Maria da Fé-MG&
Mariana-MG&
Marilac-MG&
Mário Campos-MG&
Maripá de Minas-MG&
Marliéria-MG&
Marmelópolis-MG&
Martinho Campos-MG&
Martins Soares-MG&
Mata Verde-MG&
Materlândia-MG&
Mateus Leme-MG&
Mathias Lobato-MG&
Matias Barbosa-MG&
Matias Cardoso-MG&
Matipó-MG&
Mato Verde-MG&
Matozinhos-MG&
Matutina-MG&
Medeiros-MG&
Medina-MG&
Mendes Pimentel-MG&
Mercês-MG&
Mesquita-MG&
Minas Novas-MG&
Minduri-MG&
Mirabela-MG&
Miradouro-MG&
Miraí-MG&
Miravânia-MG&
Moeda-MG&
Moema-MG&
Monjolos-MG&
Monsenhor Paulo-MG&
Montalvânia-MG&
Monte Alegre de Minas-MG&
Monte Azul-MG&
Monte Belo-MG&
Monte Carmelo-MG&
Monte Formoso-MG&
Monte Santo de Minas-MG&
Monte Sião-MG&
Montes Claros-MG&
Montezuma-MG&
Morada Nova de Minas-MG&
Morro da Garça-MG&
Morro do Pilar-MG&
Munhoz-MG&
Muriaé-MG&
Mutum-MG&
Muzambinho-MG&
Nacip Raydan-MG&
Nanuque-MG&
Naque-MG&
Natalândia-MG&
Natércia-MG&
Nazareno-MG&
Nepomuceno-MG&
Ninheira-MG&
Nova Belém-MG&
Nova Era-MG&
Nova Lima-MG&
Nova Módica-MG&
Nova Ponte-MG&
Nova Porteirinha-MG&
Nova Resende-MG&
Nova Serrana-MG&
Nova União-MG&
Novo Cruzeiro-MG&
Novo Oriente de Minas-MG&
Novorizonte-MG&
Olaria-MG&
Olhos-d'Água-MG&
Olímpio Noronha-MG&
Oliveira-MG&
Oliveira Fortes-MG&
Onça de Pitangui-MG&
Oratórios-MG&
Orizânia-MG&
Ouro Branco-MG&
Ouro Fino-MG&
Ouro Preto-MG&
Ouro Verde de Minas-MG&
Padre Carvalho-MG&
Padre Paraíso-MG&
Pai Pedro-MG&
Paineiras-MG&
Pains-MG&
Paiva-MG&
Palma-MG&
Palmópolis-MG&
Papagaios-MG&
Pará de Minas-MG&
Paracatu-MG&
Paraguaçu-MG&
Paraisópolis-MG&
Paraopeba-MG&
Passa Quatro-MG&
Passa Tempo-MG&
Passabém-MG&
Passa-Vinte-MG&
Passos-MG&
Patis-MG&
Patos de Minas-MG&
Patrocínio-MG&
Patrocínio do Muriaé-MG&
Paula Cândido-MG&
Paulistas-MG&
Pavão-MG&
Peçanha-MG&
Pedra Azul-MG&
Pedra Bonita-MG&
Pedra do Anta-MG&
Pedra do Indaiá-MG&
Pedra Dourada-MG&
Pedralva-MG&
Pedras de Maria da Cruz-MG&
Pedrinópolis-MG&
Pedro Leopoldo-MG&
Pedro Teixeira-MG&
Pequeri-MG&
Pequi-MG&
Perdigão-MG&
Perdizes-MG&
Perdões-MG&
Periquito-MG&
Pescador-MG&
Piau-MG&
Piedade de Caratinga-MG&
Piedade de Ponte Nova-MG&
Piedade do Rio Grande-MG&
Piedade dos Gerais-MG&
Pimenta-MG&
Pingo-d'Água-MG&
Pintópolis-MG&
Piracema-MG&
Pirajuba-MG&
Piranga-MG&
Piranguçu-MG&
Piranguinho-MG&
Pirapetinga-MG&
Pirapora-MG&
Piraúba-MG&
Pitangui-MG&
Piumhi-MG&
Planura-MG&
Poço Fundo-MG&
Poços de Caldas-MG&
Pocrane-MG&
Pompéu-MG&
Ponte Nova-MG&
Ponto Chique-MG&
Ponto dos Volantes-MG&
Porteirinha-MG&
Porto Firme-MG&
Poté-MG&
Pouso Alegre-MG&
Pouso Alto-MG&
Prados-MG&
Prata-MG&
Pratápolis-MG&
Pratinha-MG&
Presidente Bernardes-MG&
Presidente Juscelino-MG&
Presidente Kubitschek-MG&
Presidente Olegário-MG&
Prudente de Morais-MG&
Quartel Geral-MG&
Queluzito-MG&
Raposos-MG&
Raul Soares-MG&
Recreio-MG&
Reduto-MG&
Resende Costa-MG&
Resplendor-MG&
Ressaquinha-MG&
Riachinho-MG&
Riacho dos Machados-MG&
Ribeirão das Neves-MG&
Ribeirão Vermelho-MG&
Rio Acima-MG&
Rio Casca-MG&
Rio do Prado-MG&
Rio Doce-MG&
Rio Espera-MG&
Rio Manso-MG&
Rio Novo-MG&
Rio Paranaíba-MG&
Rio Pardo de Minas-MG&
Rio Piracicaba-MG&
Rio Pomba-MG&
Rio Preto-MG&
Rio Vermelho-MG&
Ritápolis-MG&
Rochedo de Minas-MG&
Rodeiro-MG&
Romaria-MG&
Rosário da Limeira-MG&
Rubelita-MG&
Rubim-MG&
Sabará-MG&
Sabinópolis-MG&
Sacramento-MG&
Salinas-MG&
Salto da Divisa-MG&
Santa Bárbara-MG&
Santa Bárbara do Leste-MG&
Santa Bárbara do Monte Verde-MG&
Santa Bárbara do Tugúrio-MG&
Santa Cruz de Minas-MG&
Santa Cruz de Salinas-MG&
Santa Cruz do Escalvado-MG&
Santa Efigênia de Minas-MG&
Santa Fé de Minas-MG&
Santa Helena de Minas-MG&
Santa Juliana-MG&
Santa Luzia-MG&
Santa Margarida-MG&
Santa Maria de Itabira-MG&
Santa Maria do Salto-MG&
Santa Maria do Suaçuí-MG&
Santa Rita de Caldas-MG&
Santa Rita de Ibitipoca-MG&
Santa Rita de Jacutinga-MG&
Santa Rita de Minas-MG&
Santa Rita do Itueto-MG&
Santa Rita do Sapucaí-MG&
Santa Rosa da Serra-MG&
Santa Vitória-MG&
Santana da Vargem-MG&
Santana de Cataguases-MG&
Santana de Pirapama-MG&
Santana do Deserto-MG&
Santana do Garambéu-MG&
Santana do Jacaré-MG&
Santana do Manhuaçu-MG&
Santana do Paraíso-MG&
Santana do Riacho-MG&
Santana dos Montes-MG&
Santo Antônio do Amparo-MG&
Santo Antônio do Aventureiro-MG&
Santo Antônio do Grama-MG&
Santo Antônio do Itambé-MG&
Santo Antônio do Jacinto-MG&
Santo Antônio do Monte-MG&
Santo Antônio do Retiro-MG&
Santo Antônio do Rio Abaixo-MG&
Santo Hipólito-MG&
Santos Dumont-MG&
São Bento Abade-MG&
São Brás do Suaçuí-MG&
São Domingos das Dores-MG&
São Domingos do Prata-MG&
São Félix de Minas-MG&
São Francisco-MG&
São Francisco de Paula-MG&
São Francisco de Sales-MG&
São Francisco do Glória-MG&
São Geraldo-MG&
São Geraldo da Piedade-MG&
São Geraldo do Baixio-MG&
São Gonçalo do Abaeté-MG&
São Gonçalo do Pará-MG&
São Gonçalo do Rio Abaixo-MG&
São Gonçalo do Rio Preto-MG&
São Gonçalo do Sapucaí-MG&
São Gotardo-MG&
São João Batista do Glória-MG&
São João da Lagoa-MG&
São João da Mata-MG&
São João da Ponte-MG&
São João das Missões-MG&
São João del Rei-MG&
São João do Manhuaçu-MG&
São João do Manteninha-MG&
São João do Oriente-MG&
São João do Pacuí-MG&
São João do Paraíso-MG&
São João Evangelista-MG&
São João Nepomuceno-MG&
São Joaquim de Bicas-MG&
São José da Barra-MG&
São José da Lapa-MG&
São José da Safira-MG&
São José da Varginha-MG&
São José do Alegre-MG&
São José do Divino-MG&
São José do Goiabal-MG&
São José do Jacuri-MG&
São José do Mantimento-MG&
São Lourenço-MG&
São Miguel do Anta-MG&
São Pedro da União-MG&
São Pedro do Suaçuí-MG&
São Pedro dos Ferros-MG&
São Romão-MG&
São Roque de Minas-MG&
São Sebastião da Bela Vista-MG&
São Sebastião da Vargem Alegre-MG&
São Sebastião do Anta-MG&
São Sebastião do Maranhão-MG&
São Sebastião do Oeste-MG&
São Sebastião do Paraíso-MG&
São Sebastião do Rio Preto-MG&
São Sebastião do Rio Verde-MG&
São Thomé das Letras-MG&
São Tiago-MG&
São Tomás de Aquino-MG&
São Vicente de Minas-MG&
Sapucaí-Mirim-MG&
Sardoá-MG&
Sarzedo-MG&
Sem-Peixe-MG&
Senador Amaral-MG&
Senador Cortes-MG&
Senador Firmino-MG&
Senador José Bento-MG&
Senador Modestino Gonçalves-MG&
Senhora de Oliveira-MG&
Senhora do Porto-MG&
Senhora dos Remédios-MG&
Sericita-MG&
Seritinga-MG&
Serra Azul de Minas-MG&
Serra da Saudade-MG&
Serra do Salitre-MG&
Serra dos Aimorés-MG&
Serrania-MG&
Serranópolis de Minas-MG&
Serranos-MG&
Serro-MG&
Sete Lagoas-MG&
Setubinha-MG&
Silveirânia-MG&
Silvianópolis-MG&
Simão Pereira-MG&
Simonésia-MG&
Sobrália-MG&
Soledade de Minas-MG&
Tabuleiro-MG&
Taiobeiras-MG&
Taparuba-MG&
Tapira-MG&
Tapiraí-MG&
Taquaraçu de Minas-MG&
Tarumirim-MG&
Teixeiras-MG&
Teófilo Otoni-MG&
Timóteo-MG&
Tiradentes-MG&
Tiros-MG&
Tocantins-MG&
Tocos do Moji-MG&
Toledo-MG&
Tombos-MG&
Três Corações-MG&
Três Marias-MG&
Três Pontas-MG&
Tumiritinga-MG&
Tupaciguara-MG&
Turmalina-MG&
Turvolândia-MG&
Ubá-MG&
Ubaí-MG&
Ubaporanga-MG&
Uberaba-MG&
Uberlândia-MG&
Umburatiba-MG&
Unaí-MG&
União de Minas-MG&
Uruana de Minas-MG&
Urucânia-MG&
Urucuia-MG&
Vargem Alegre-MG&
Vargem Bonita-MG&
Vargem Grande do Rio Pardo-MG&
Varginha-MG&
Varjão de Minas-MG&
Várzea da Palma-MG&
Varzelândia-MG&
Vazante-MG&
Verdelândia-MG&
Veredinha-MG&
Veríssimo-MG&
Vermelho Novo-MG&
Vespasiano-MG&
Viçosa-MG&
Vieiras-MG&
Virgem da Lapa-MG&
Virgínia-MG&
Virginópolis-MG&
Virgolândia-MG&
Visconde do Rio Branco-MG&
Volta Grande-MG&
Wenceslau Braz-MG&
Afonso Cláudio-ES&
Água Doce do Norte-ES&
Águia Branca-ES&
Alegre-ES&
Alfredo Chaves-ES&
Alto Rio Novo-ES&
Anchieta-ES&
Apiacá-ES&
Aracruz-ES&
Atilio Vivacqua-ES&
Baixo Guandu-ES&
Barra de São Francisco-ES&
Boa Esperança-ES&
Bom Jesus do Norte-ES&
Brejetuba-ES&
Cachoeiro de Itapemirim-ES&
Cariacica-ES&
Castelo-ES&
Colatina-ES&
Conceição da Barra-ES&
Conceição do Castelo-ES&
Divino de São Lourenço-ES&
Domingos Martins-ES&
Dores do Rio Preto-ES&
Ecoporanga-ES&
Fundão-ES&
Governador Lindenberg-ES&
Guaçuí-ES&
Guarapari-ES&
Ibatiba-ES&
Ibiraçu-ES&
Ibitirama-ES&
Iconha-ES&
Irupi-ES&
Itaguaçu-ES&
Itapemirim-ES&
Itarana-ES&
Iúna-ES&
Jaguaré-ES&
Jerônimo Monteiro-ES&
João Neiva-ES&
Laranja da Terra-ES&
Linhares-ES&
Mantenópolis-ES&
Marataízes-ES&
Marechal Floriano-ES&
Marilândia-ES&
Mimoso do Sul-ES&
Montanha-ES&
Mucurici-ES&
Muniz Freire-ES&
Muqui-ES&
Nova Venécia-ES&
Pancas-ES&
Pedro Canário-ES&
Pinheiros-ES&
Piúma-ES&
Ponto Belo-ES&
Presidente Kennedy-ES&
Rio Bananal-ES&
Rio Novo do Sul-ES&
Santa Leopoldina-ES&
Santa Maria de Jetibá-ES&
Santa Teresa-ES&
São Domingos do Norte-ES&
São Gabriel da Palha-ES&
São José do Calçado-ES&
São Mateus-ES&
São Roque do Canaã-ES&
Serra-ES&
Sooretama-ES&
Vargem Alta-ES&
Venda Nova do Imigrante-ES&
Viana-ES&
Vila Pavão-ES&
Vila Valério-ES&
Vila Velha-ES&
Vitória-ES&
Angra dos Reis-RJ&
Aperibé-RJ&
Araruama-RJ&
Areal-RJ&
Armação dos Búzios-RJ&
Arraial do Cabo-RJ&
Barra do Piraí-RJ&
Barra Mansa-RJ&
Belford Roxo-RJ&
Bom Jardim-RJ&
Bom Jesus do Itabapoana-RJ&
Cabo Frio-RJ&
Cachoeiras de Macacu-RJ&
Cambuci-RJ&
Campos dos Goytacazes-RJ&
Cantagalo-RJ&
Carapebus-RJ&
Cardoso Moreira-RJ&
Carmo-RJ&
Casimiro de Abreu-RJ&
Comendador Levy Gasparian-RJ&
Conceição de Macabu-RJ&
Cordeiro-RJ&
Duas Barras-RJ&
Duque de Caxias-RJ&
Engenheiro Paulo de Frontin-RJ&
Guapimirim-RJ&
Iguaba Grande-RJ&
Itaboraí-RJ&
Itaguaí-RJ&
Italva-RJ&
Itaocara-RJ&
Itaperuna-RJ&
Itatiaia-RJ&
Japeri-RJ&
Laje do Muriaé-RJ&
Macaé-RJ&
Macuco-RJ&
Magé-RJ&
Mangaratiba-RJ&
Maricá-RJ&
Mendes-RJ&
Mesquita-RJ&
Miguel Pereira-RJ&
Miracema-RJ&
Natividade-RJ&
Nilópolis-RJ&
Niterói-RJ&
Nova Friburgo-RJ&
Nova Iguaçu-RJ&
Paracambi-RJ&
Paraíba do Sul-RJ&
Parati-RJ&
Paty do Alferes-RJ&
Petrópolis-RJ&
Pinheiral-RJ&
Piraí-RJ&
Porciúncula-RJ&
Porto Real-RJ&
Quatis-RJ&
Queimados-RJ&
Quissamã-RJ&
Resende-RJ&
Rio Bonito-RJ&
Rio Claro-RJ&
Rio das Flores-RJ&
Rio das Ostras-RJ&
Rio de Janeiro-RJ&
Santa Maria Madalena-RJ&
Santo Antônio de Pádua-RJ&
São Fidélis-RJ&
São Francisco de Itabapoana-RJ&
São Gonçalo-RJ&
São João da Barra-RJ&
São João de Meriti-RJ&
São José de Ubá-RJ&
São José do Vale do Rio Preto-RJ&
São Pedro da Aldeia-RJ&
São Sebastião do Alto-RJ&
Sapucaia-RJ&
Saquarema-RJ&
Seropédica-RJ&
Silva Jardim-RJ&
Sumidouro-RJ&
Tanguá-RJ&
Teresópolis-RJ&
Trajano de Morais-RJ&
Três Rios-RJ&
Valença-RJ&
Varre-Sai-RJ&
Vassouras-RJ&
Volta Redonda-RJ&
Adamantina-SP&
Adolfo-SP&
Aguaí-SP&
Águas da Prata-SP&
Águas de Lindóia-SP&
Águas de Santa Bárbara-SP&
Águas de São Pedro-SP&
Agudos-SP&
Alambari-SP&
Alfredo Marcondes-SP&
Altair-SP&
Altinópolis-SP&
Alto Alegre-SP&
Alumínio-SP&
Álvares Florence-SP&
Álvares Machado-SP&
Álvaro de Carvalho-SP&
Alvinlândia-SP&
Americana-SP&
Américo Brasiliense-SP&
Américo de Campos-SP&
Amparo-SP&
Analândia-SP&
Andradina-SP&
Angatuba-SP&
Anhembi-SP&
Anhumas-SP&
Aparecida-SP&
Aparecida d'Oeste-SP&
Apiaí-SP&
Araçariguama-SP&
Araçatuba-SP&
Araçoiaba da Serra-SP&
Aramina-SP&
Arandu-SP&
Arapeí-SP&
Araraquara-SP&
Araras-SP&
Arco-Íris-SP&
Arealva-SP&
Areias-SP&
Areiópolis-SP&
Ariranha-SP&
Artur Nogueira-SP&
Arujá-SP&
Aspásia-SP&
Assis-SP&
Atibaia-SP&
Auriflama-SP&
Avaí-SP&
Avanhandava-SP&
Avaré-SP&
Bady Bassitt-SP&
Balbinos-SP&
Bálsamo-SP&
Bananal-SP&
Barão de Antonina-SP&
Barbosa-SP&
Bariri-SP&
Barra Bonita-SP&
Barra do Chapéu-SP&
Barra do Turvo-SP&
Barretos-SP&
Barrinha-SP&
Barueri-SP&
Bastos-SP&
Batatais-SP&
Bauru-SP&
Bebedouro-SP&
Bento de Abreu-SP&
Bernardino de Campos-SP&
Bertioga-SP&
Bilac-SP&
Birigui-SP&
Biritiba-Mirim-SP&
Boa Esperança do Sul-SP&
Bocaina-SP&
Bofete-SP&
Boituva-SP&
Bom Jesus dos Perdões-SP&
Bom Sucesso de Itararé-SP&
Borá-SP&
Boracéia-SP&
Borborema-SP&
Borebi-SP&
Botucatu-SP&
Bragança Paulista-SP&
Braúna-SP&
Brejo Alegre-SP&
Brodowski-SP&
Brotas-SP&
Buri-SP&
Buritama-SP&
Buritizal-SP&
Cabrália Paulista-SP&
Cabreúva-SP&
Caçapava-SP&
Cachoeira Paulista-SP&
Caconde-SP&
Cafelândia-SP&
Caiabu-SP&
Caieiras-SP&
Caiuá-SP&
Cajamar-SP&
Cajati-SP&
Cajobi-SP&
Cajuru-SP&
Campina do Monte Alegre-SP&
Campinas-SP&
Campo Limpo Paulista-SP&
Campos do Jordão-SP&
Campos Novos Paulista-SP&
Cananéia-SP&
Canas-SP&
Cândido Mota-SP&
Cândido Rodrigues-SP&
Canitar-SP&
Capão Bonito-SP&
Capela do Alto-SP&
Capivari-SP&
Caraguatatuba-SP&
Carapicuíba-SP&
Cardoso-SP&
Casa Branca-SP&
Cássia dos Coqueiros-SP&
Castilho-SP&
Catanduva-SP&
Catiguá-SP&
Cedral-SP&
Cerqueira César-SP&
Cerquilho-SP&
Cesário Lange-SP&
Charqueada-SP&
Chavantes-SP&
Clementina-SP&
Colina-SP&
Colômbia-SP&
Conchal-SP&
Conchas-SP&
Cordeirópolis-SP&
Coroados-SP&
Coronel Macedo-SP&
Corumbataí-SP&
Cosmópolis-SP&
Cosmorama-SP&
Cotia-SP&
Cravinhos-SP&
Cristais Paulista-SP&
Cruzália-SP&
Cruzeiro-SP&
Cubatão-SP&
Cunha-SP&
Descalvado-SP&
Diadema-SP&
Dirce Reis-SP&
Divinolândia-SP&
Dobrada-SP&
Dois Córregos-SP&
Dolcinópolis-SP&
Dourado-SP&
Dracena-SP&
Duartina-SP&
Dumont-SP&
Echaporã-SP&
Eldorado-SP&
Elias Fausto-SP&
Elisiário-SP&
Embaúba-SP&
Embu-SP&
Embu-Guaçu-SP&
Emilianópolis-SP&
Engenheiro Coelho-SP&
Espírito Santo do Pinhal-SP&
Espírito Santo do Turvo-SP&
Estiva Gerbi-SP&
Estrela do Norte-SP&
Estrela d'Oeste-SP&
Euclides da Cunha Paulista-SP&
Fartura-SP&
Fernando Prestes-SP&
Fernandópolis-SP&
Fernão-SP&
Ferraz de Vasconcelos-SP&
Flora Rica-SP&
Floreal-SP&
Flórida Paulista-SP&
Florínia-SP&
Franca-SP&
Francisco Morato-SP&
Franco da Rocha-SP&
Gabriel Monteiro-SP&
Gália-SP&
Garça-SP&
Gastão Vidigal-SP&
Gavião Peixoto-SP&
General Salgado-SP&
Getulina-SP&
Glicério-SP&
Guaiçara-SP&
Guaimbê-SP&
Guaíra-SP&
Guapiaçu-SP&
Guapiara-SP&
Guará-SP&
Guaraçaí-SP&
Guaraci-SP&
Guarani d'Oeste-SP&
Guarantã-SP&
Guararapes-SP&
Guararema-SP&
Guaratinguetá-SP&
Guareí-SP&
Guariba-SP&
Guarujá-SP&
Guarulhos-SP&
Guatapará-SP&
Guzolândia-SP&
Herculândia-SP&
Holambra-SP&
Hortolândia-SP&
Iacanga-SP&
Iacri-SP&
Iaras-SP&
Ibaté-SP&
Ibirá-SP&
Ibirarema-SP&
Ibitinga-SP&
Ibiúna-SP&
Icém-SP&
Iepê-SP&
Igaraçu do Tietê-SP&
Igarapava-SP&
Igaratá-SP&
Iguape-SP&
Ilha Comprida-SP&
Ilha Solteira-SP&
Ilhabela-SP&
Indaiatuba-SP&
Indiana-SP&
Indiaporã-SP&
Inúbia Paulista-SP&
Ipaussu-SP&
Iperó-SP&
Ipeúna-SP&
Ipiguá-SP&
Iporanga-SP&
Ipuã-SP&
Iracemápolis-SP&
Irapuã-SP&
Irapuru-SP&
Itaberá-SP&
Itaí-SP&
Itajobi-SP&
Itaju-SP&
Itanhaém-SP&
Itaóca-SP&
Itapecerica da Serra-SP&
Itapetininga-SP&
Itapeva-SP&
Itapevi-SP&
Itapira-SP&
Itapirapuã Paulista-SP&
Itápolis-SP&
Itaporanga-SP&
Itapuí-SP&
Itapura-SP&
Itaquaquecetuba-SP&
Itararé-SP&
Itariri-SP&
Itatiba-SP&
Itatinga-SP&
Itirapina-SP&
Itirapuã-SP&
Itobi-SP&
Itu-SP&
Itupeva-SP&
Ituverava-SP&
Jaborandi-SP&
Jaboticabal-SP&
Jacareí-SP&
Jaci-SP&
Jacupiranga-SP&
Jaguariúna-SP&
Jales-SP&
Jambeiro-SP&
Jandira-SP&
Jardinópolis-SP&
Jarinu-SP&
Jaú-SP&
Jeriquara-SP&
Joanópolis-SP&
João Ramalho-SP&
José Bonifácio-SP&
Júlio Mesquita-SP&
Jumirim-SP&
Jundiaí-SP&
Junqueirópolis-SP&
Juquiá-SP&
Juquitiba-SP&
Lagoinha-SP&
Laranjal Paulista-SP&
Lavínia-SP&
Lavrinhas-SP&
Leme-SP&
Lençóis Paulista-SP&
Limeira-SP&
Lindóia-SP&
Lins-SP&
Lorena-SP&
Lourdes-SP&
Louveira-SP&
Lucélia-SP&
Lucianópolis-SP&
Luís Antônio-SP&
Luiziânia-SP&
Lupércio-SP&
Lutécia-SP&
Macatuba-SP&
Macaubal-SP&
Macedônia-SP&
Magda-SP&
Mairinque-SP&
Mairiporã-SP&
Manduri-SP&
Marabá Paulista-SP&
Maracaí-SP&
Marapoama-SP&
Mariápolis-SP&
Marília-SP&
Marinópolis-SP&
Martinópolis-SP&
Matão-SP&
Mauá-SP&
Mendonça-SP&
Meridiano-SP&
Mesópolis-SP&
Miguelópolis-SP&
Mineiros do Tietê-SP&
Mira Estrela-SP&
Miracatu-SP&
Mirandópolis-SP&
Mirante do Paranapanema-SP&
Mirassol-SP&
Mirassolândia-SP&
Mococa-SP&
Mogi das Cruzes-SP&
Mogi Guaçu-SP&
Moji Mirim-SP&
Mombuca-SP&
Monções-SP&
Mongaguá-SP&
Monte Alegre do Sul-SP&
Monte Alto-SP&
Monte Aprazível-SP&
Monte Azul Paulista-SP&
Monte Castelo-SP&
Monte Mor-SP&
Monteiro Lobato-SP&
Morro Agudo-SP&
Morungaba-SP&
Motuca-SP&
Murutinga do Sul-SP&
Nantes-SP&
Narandiba-SP&
Natividade da Serra-SP&
Nazaré Paulista-SP&
Neves Paulista-SP&
Nhandeara-SP&
Nipoã-SP&
Nova Aliança-SP&
Nova Campina-SP&
Nova Canaã Paulista-SP&
Nova Castilho-SP&
Nova Europa-SP&
Nova Granada-SP&
Nova Guataporanga-SP&
Nova Independência-SP&
Nova Luzitânia-SP&
Nova Odessa-SP&
Novais-SP&
Novo Horizonte-SP&
Nuporanga-SP&
Ocauçu-SP&
Óleo-SP&
Olímpia-SP&
Onda Verde-SP&
Oriente-SP&
Orindiúva-SP&
Orlândia-SP&
Osasco-SP&
Oscar Bressane-SP&
Osvaldo Cruz-SP&
Ourinhos-SP&
Ouro Verde-SP&
Ouroeste-SP&
Pacaembu-SP&
Palestina-SP&
Palmares Paulista-SP&
Palmeira d'Oeste-SP&
Palmital-SP&
Panorama-SP&
Paraguaçu Paulista-SP&
Paraibuna-SP&
Paraíso-SP&
Paranapanema-SP&
Paranapuã-SP&
Parapuã-SP&
Pardinho-SP&
Pariquera-Açu-SP&
Parisi-SP&
Patrocínio Paulista-SP&
Paulicéia-SP&
Paulínia-SP&
Paulistânia-SP&
Paulo de Faria-SP&
Pederneiras-SP&
Pedra Bela-SP&
Pedranópolis-SP&
Pedregulho-SP&
Pedreira-SP&
Pedrinhas Paulista-SP&
Pedro de Toledo-SP&
Penápolis-SP&
Pereira Barreto-SP&
Pereiras-SP&
Peruíbe-SP&
Piacatu-SP&
Piedade-SP&
Pilar do Sul-SP&
Pindamonhangaba-SP&
Pindorama-SP&
Pinhalzinho-SP&
Piquerobi-SP&
Piquete-SP&
Piracaia-SP&
Piracicaba-SP&
Piraju-SP&
Pirajuí-SP&
Pirangi-SP&
Pirapora do Bom Jesus-SP&
Pirapozinho-SP&
Pirassununga-SP&
Piratininga-SP&
Pitangueiras-SP&
Planalto-SP&
Platina-SP&
Poá-SP&
Poloni-SP&
Pompéia-SP&
Pongaí-SP&
Pontal-SP&
Pontalinda-SP&
Pontes Gestal-SP&
Populina-SP&
Porangaba-SP&
Porto Feliz-SP&
Porto Ferreira-SP&
Potim-SP&
Potirendaba-SP&
Pracinha-SP&
Pradópolis-SP&
Praia Grande-SP&
Pratânia-SP&
Presidente Alves-SP&
Presidente Bernardes-SP&
Presidente Epitácio-SP&
Presidente Prudente-SP&
Presidente Venceslau-SP&
Promissão-SP&
Quadra-SP&
Quatá-SP&
Queiroz-SP&
Queluz-SP&
Quintana-SP&
Rafard-SP&
Rancharia-SP&
Redenção da Serra-SP&
Regente Feijó-SP&
Reginópolis-SP&
Registro-SP&
Restinga-SP&
Ribeira-SP&
Ribeirão Bonito-SP&
Ribeirão Branco-SP&
Ribeirão Corrente-SP&
Ribeirão do Sul-SP&
Ribeirão dos Índios-SP&
Ribeirão Grande-SP&
Ribeirão Pires-SP&
Ribeirão Preto-SP&
Rifaina-SP&
Rincão-SP&
Rinópolis-SP&
Rio Claro-SP&
Rio das Pedras-SP&
Rio Grande da Serra-SP&
Riolândia-SP&
Riversul-SP&
Rosana-SP&
Roseira-SP&
Rubiácea-SP&
Rubinéia-SP&
Sabino-SP&
Sagres-SP&
Sales-SP&
Sales Oliveira-SP&
Salesópolis-SP&
Salmourão-SP&
Saltinho-SP&
Salto-SP&
Salto de Pirapora-SP&
Salto Grande-SP&
Sandovalina-SP&
Santa Adélia-SP&
Santa Albertina-SP&
Santa Bárbara d'Oeste-SP&
Santa Branca-SP&
Santa Clara d'Oeste-SP&
Santa Cruz da Conceição-SP&
Santa Cruz da Esperança-SP&
Santa Cruz das Palmeiras-SP&
Santa Cruz do Rio Pardo-SP&
Santa Ernestina-SP&
Santa Fé do Sul-SP&
Santa Gertrudes-SP&
Santa Isabel-SP&
Santa Lúcia-SP&
Santa Maria da Serra-SP&
Santa Mercedes-SP&
Santa Rita do Passa Quatro-SP&
Santa Rita d'Oeste-SP&
Santa Rosa de Viterbo-SP&
Santa Salete-SP&
Santana da Ponte Pensa-SP&
Santana de Parnaíba-SP&
Santo Anastácio-SP&
Santo André-SP&
Santo Antônio da Alegria-SP&
Santo Antônio de Posse-SP&
Santo Antônio do Aracanguá-SP&
Santo Antônio do Jardim-SP&
Santo Antônio do Pinhal-SP&
Santo Expedito-SP&
Santópolis do Aguapeí-SP&
Santos-SP&
São Bento do Sapucaí-SP&
São Bernardo do Campo-SP&
São Caetano do Sul-SP&
São Carlos-SP&
São Francisco-SP&
São João da Boa Vista-SP&
São João das Duas Pontes-SP&
São João de Iracema-SP&
São João do Pau d'Alho-SP&
São Joaquim da Barra-SP&
São José da Bela Vista-SP&
São José do Barreiro-SP&
São José do Rio Pardo-SP&
São José do Rio Preto-SP&
São José dos Campos-SP&
São Lourenço da Serra-SP&
São Luís do Paraitinga-SP&
São Manuel-SP&
São Miguel Arcanjo-SP&
São Paulo-SP&
São Pedro-SP&
São Pedro do Turvo-SP&
São Roque-SP&
São Sebastião-SP&
São Sebastião da Grama-SP&
São Simão-SP&
São Vicente-SP&
Sarapuí-SP&
Sarutaiá-SP&
Sebastianópolis do Sul-SP&
Serra Azul-SP&
Serra Negra-SP&
Serrana-SP&
Sertãozinho-SP&
Sete Barras-SP&
Severínia-SP&
Silveiras-SP&
Socorro-SP&
Sorocaba-SP&
Sud Mennucci-SP&
Sumaré-SP&
Suzanápolis-SP&
Suzano-SP&
Tabapuã-SP&
Tabatinga-SP&
Taboão da Serra-SP&
Taciba-SP&
Taguaí-SP&
Taiaçu-SP&
Taiúva-SP&
Tambaú-SP&
Tanabi-SP&
Tapiraí-SP&
Tapiratiba-SP&
Taquaral-SP&
Taquaritinga-SP&
Taquarituba-SP&
Taquarivaí-SP&
Tarabai-SP&
Tarumã-SP&
Tatuí-SP&
Taubaté-SP&
Tejupá-SP&
Teodoro Sampaio-SP&
Terra Roxa-SP&
Tietê-SP&
Timburi-SP&
Torre de Pedra-SP&
Torrinha-SP&
Trabiju-SP&
Tremembé-SP&
Três Fronteiras-SP&
Tuiuti-SP&
Tupã-SP&
Tupi Paulista-SP&
Turiúba-SP&
Turmalina-SP&
Ubarana-SP&
Ubatuba-SP&
Ubirajara-SP&
Uchoa-SP&
União Paulista-SP&
Urânia-SP&
Uru-SP&
Urupês-SP&
Valentim Gentil-SP&
Valinhos-SP&
Valparaíso-SP&
Vargem-SP&
Vargem Grande do Sul-SP&
Vargem Grande Paulista-SP&
Várzea Paulista-SP&
Vera Cruz-SP&
Vinhedo-SP&
Viradouro-SP&
Vista Alegre do Alto-SP&
Vitória Brasil-SP&
Votorantim-SP&
Votuporanga-SP&
Zacarias-SP&
Abatiá-PR&
Adrianópolis-PR&
Agudos do Sul-PR&
Almirante Tamandaré-PR&
Altamira do Paraná-PR&
Alto Paraíso-PR&
Alto Paraná-PR&
Alto Piquiri-PR&
Altônia-PR&
Alvorada do Sul-PR&
Amaporã-PR&
Ampére-PR&
Anahy-PR&
Andirá-PR&
Ângulo-PR&
Antonina-PR&
Antônio Olinto-PR&
Apucarana-PR&
Arapongas-PR&
Arapoti-PR&
Arapuã-PR&
Araruna-PR&
Araucária-PR&
Ariranha do Ivaí-PR&
Assaí-PR&
Assis Chateaubriand-PR&
Astorga-PR&
Atalaia-PR&
Balsa Nova-PR&
Bandeirantes-PR&
Barbosa Ferraz-PR&
Barra do Jacaré-PR&
Barracão-PR&
Bela Vista da Caroba-PR&
Bela Vista do Paraíso-PR&
Bituruna-PR&
Boa Esperança-PR&
Boa Esperança do Iguaçu-PR&
Boa Ventura de São Roque-PR&
Boa Vista da Aparecida-PR&
Bocaiúva do Sul-PR&
Bom Jesus do Sul-PR&
Bom Sucesso-PR&
Bom Sucesso do Sul-PR&
Borrazópolis-PR&
Braganey-PR&
Brasilândia do Sul-PR&
Cafeara-PR&
Cafelândia-PR&
Cafezal do Sul-PR&
Califórnia-PR&
Cambará-PR&
Cambé-PR&
Cambira-PR&
Campina da Lagoa-PR&
Campina do Simão-PR&
Campina Grande do Sul-PR&
Campo Bonito-PR&
Campo do Tenente-PR&
Campo Largo-PR&
Campo Magro-PR&
Campo Mourão-PR&
Cândido de Abreu-PR&
Candói-PR&
Cantagalo-PR&
Capanema-PR&
Capitão Leônidas Marques-PR&
Carambeí-PR&
Carlópolis-PR&
Cascavel-PR&
Castro-PR&
Catanduvas-PR&
Centenário do Sul-PR&
Cerro Azul-PR&
Céu Azul-PR&
Chopinzinho-PR&
Cianorte-PR&
Cidade Gaúcha-PR&
Clevelândia-PR&
Colombo-PR&
Colorado-PR&
Congonhinhas-PR&
Conselheiro Mairinck-PR&
Contenda-PR&
Corbélia-PR&
Cornélio Procópio-PR&
Coronel Domingos Soares-PR&
Coronel Vivida-PR&
Corumbataí do Sul-PR&
Cruz Machado-PR&
Cruzeiro do Iguaçu-PR&
Cruzeiro do Oeste-PR&
Cruzeiro do Sul-PR&
Cruzmaltina-PR&
Curitiba-PR&
Curiúva-PR&
Diamante do Norte-PR&
Diamante do Sul-PR&
Diamante D'Oeste-PR&
Dois Vizinhos-PR&
Douradina-PR&
Doutor Camargo-PR&
Doutor Ulysses-PR&
Enéas Marques-PR&
Engenheiro Beltrão-PR&
Entre Rios do Oeste-PR&
Esperança Nova-PR&
Espigão Alto do Iguaçu-PR&
Farol-PR&
Faxinal-PR&
Fazenda Rio Grande-PR&
Fênix-PR&
Fernandes Pinheiro-PR&
Figueira-PR&
Flor da Serra do Sul-PR&
Floraí-PR&
Floresta-PR&
Florestópolis-PR&
Flórida-PR&
Formosa do Oeste-PR&
Foz do Iguaçu-PR&
Foz do Jordão-PR&
Francisco Alves-PR&
Francisco Beltrão-PR&
General Carneiro-PR&
Godoy Moreira-PR&
Goioerê-PR&
Goioxim-PR&
Grandes Rios-PR&
Guaíra-PR&
Guairaçá-PR&
Guamiranga-PR&
Guapirama-PR&
Guaporema-PR&
Guaraci-PR&
Guaraniaçu-PR&
Guarapuava-PR&
Guaraqueçaba-PR&
Guaratuba-PR&
Honório Serpa-PR&
Ibaiti-PR&
Ibema-PR&
Ibiporã-PR&
Icaraíma-PR&
Iguaraçu-PR&
Iguatu-PR&
Imbaú-PR&
Imbituva-PR&
Inácio Martins-PR&
Inajá-PR&
Indianópolis-PR&
Ipiranga-PR&
Iporã-PR&
Iracema do Oeste-PR&
Irati-PR&
Iretama-PR&
Itaguajé-PR&
Itaipulândia-PR&
Itambaracá-PR&
Itambé-PR&
Itapejara d'Oeste-PR&
Itaperuçu-PR&
Itaúna do Sul-PR&
Ivaí-PR&
Ivaiporã-PR&
Ivaté-PR&
Ivatuba-PR&
Jaboti-PR&
Jacarezinho-PR&
Jaguapitã-PR&
Jaguariaíva-PR&
Jandaia do Sul-PR&
Janiópolis-PR&
Japira-PR&
Japurá-PR&
Jardim Alegre-PR&
Jardim Olinda-PR&
Jataizinho-PR&
Jesuítas-PR&
Joaquim Távora-PR&
Jundiaí do Sul-PR&
Juranda-PR&
Jussara-PR&
Kaloré-PR&
Lapa-PR&
Laranjal-PR&
Laranjeiras do Sul-PR&
Leópolis-PR&
Lidianópolis-PR&
Lindoeste-PR&
Loanda-PR&
Lobato-PR&
Londrina-PR&
Luiziana-PR&
Lunardelli-PR&
Lupionópolis-PR&
Mallet-PR&
Mamborê-PR&
Mandaguaçu-PR&
Mandaguari-PR&
Mandirituba-PR&
Manfrinópolis-PR&
Mangueirinha-PR&
Manoel Ribas-PR&
Marechal Cândido Rondon-PR&
Maria Helena-PR&
Marialva-PR&
Marilândia do Sul-PR&
Marilena-PR&
Mariluz-PR&
Maringá-PR&
Mariópolis-PR&
Maripá-PR&
Marmeleiro-PR&
Marquinho-PR&
Marumbi-PR&
Matelândia-PR&
Matinhos-PR&
Mato Rico-PR&
Mauá da Serra-PR&
Medianeira-PR&
Mercedes-PR&
Mirador-PR&
Miraselva-PR&
Missal-PR&
Moreira Sales-PR&
Morretes-PR&
Munhoz de Melo-PR&
Nossa Senhora das Graças-PR&
Nova Aliança do Ivaí-PR&
Nova América da Colina-PR&
Nova Aurora-PR&
Nova Cantu-PR&
Nova Esperança-PR&
Nova Esperança do Sudoeste-PR&
Nova Fátima-PR&
Nova Laranjeiras-PR&
Nova Londrina-PR&
Nova Olímpia-PR&
Nova Prata do Iguaçu-PR&
Nova Santa Bárbara-PR&
Nova Santa Rosa-PR&
Nova Tebas-PR&
Novo Itacolomi-PR&
Ortigueira-PR&
Ourizona-PR&
Ouro Verde do Oeste-PR&
Paiçandu-PR&
Palmas-PR&
Palmeira-PR&
Palmital-PR&
Palotina-PR&
Paraíso do Norte-PR&
Paranacity-PR&
Paranaguá-PR&
Paranapoema-PR&
Paranavaí-PR&
Pato Bragado-PR&
Pato Branco-PR&
Paula Freitas-PR&
Paulo Frontin-PR&
Peabiru-PR&
Perobal-PR&
Pérola-PR&
Pérola d'Oeste-PR&
Piên-PR&
Pinhais-PR&
Pinhal de São Bento-PR&
Pinhalão-PR&
Pinhão-PR&
Piraí do Sul-PR&
Piraquara-PR&
Pitanga-PR&
Pitangueiras-PR&
Planaltina do Paraná-PR&
Planalto-PR&
Ponta Grossa-PR&
Pontal do Paraná-PR&
Porecatu-PR&
Porto Amazonas-PR&
Porto Barreiro-PR&
Porto Rico-PR&
Porto Vitória-PR&
Prado Ferreira-PR&
Pranchita-PR&
Presidente Castelo Branco-PR&
Primeiro de Maio-PR&
Prudentópolis-PR&
Quarto Centenário-PR&
Quatiguá-PR&
Quatro Barras-PR&
Quatro Pontes-PR&
Quedas do Iguaçu-PR&
Querência do Norte-PR&
Quinta do Sol-PR&
Quitandinha-PR&
Ramilândia-PR&
Rancho Alegre-PR&
Rancho Alegre D'Oeste-PR&
Realeza-PR&
Rebouças-PR&
Renascença-PR&
Reserva-PR&
Reserva do Iguaçu-PR&
Ribeirão Claro-PR&
Ribeirão do Pinhal-PR&
Rio Azul-PR&
Rio Bom-PR&
Rio Bonito do Iguaçu-PR&
Rio Branco do Ivaí-PR&
Rio Branco do Sul-PR&
Rio Negro-PR&
Rolândia-PR&
Roncador-PR&
Rondon-PR&
Rosário do Ivaí-PR&
Sabáudia-PR&
Salgado Filho-PR&
Salto do Itararé-PR&
Salto do Lontra-PR&
Santa Amélia-PR&
Santa Cecília do Pavão-PR&
Santa Cruz de Monte Castelo-PR&
Santa Fé-PR&
Santa Helena-PR&
Santa Inês-PR&
Santa Isabel do Ivaí-PR&
Santa Izabel do Oeste-PR&
Santa Lúcia-PR&
Santa Maria do Oeste-PR&
Santa Mariana-PR&
Santa Mônica-PR&
Santa Tereza do Oeste-PR&
Santa Terezinha de Itaipu-PR&
Santana do Itararé-PR&
Santo Antônio da Platina-PR&
Santo Antônio do Caiuá-PR&
Santo Antônio do Paraíso-PR&
Santo Antônio do Sudoeste-PR&
Santo Inácio-PR&
São Carlos do Ivaí-PR&
São Jerônimo da Serra-PR&
São João-PR&
São João do Caiuá-PR&
São João do Ivaí-PR&
São João do Triunfo-PR&
São Jorge do Ivaí-PR&
São Jorge do Patrocínio-PR&
São Jorge d'Oeste-PR&
São José da Boa Vista-PR&
São José das Palmeiras-PR&
São José dos Pinhais-PR&
São Manoel do Paraná-PR&
São Mateus do Sul-PR&
São Miguel do Iguaçu-PR&
São Pedro do Iguaçu-PR&
São Pedro do Ivaí-PR&
São Pedro do Paraná-PR&
São Sebastião da Amoreira-PR&
São Tomé-PR&
Sapopema-PR&
Sarandi-PR&
Saudade do Iguaçu-PR&
Sengés-PR&
Serranópolis do Iguaçu-PR&
Sertaneja-PR&
Sertanópolis-PR&
Siqueira Campos-PR&
Sulina-PR&
Tamarana-PR&
Tamboara-PR&
Tapejara-PR&
Tapira-PR&
Teixeira Soares-PR&
Telêmaco Borba-PR&
Terra Boa-PR&
Terra Rica-PR&
Terra Roxa-PR&
Tibagi-PR&
Tijucas do Sul-PR&
Toledo-PR&
Tomazina-PR&
Três Barras do Paraná-PR&
Tunas do Paraná-PR&
Tuneiras do Oeste-PR&
Tupãssi-PR&
Turvo-PR&
Ubiratã-PR&
Umuarama-PR&
União da Vitória-PR&
Uniflor-PR&
Uraí-PR&
Ventania-PR&
Vera Cruz do Oeste-PR&
Verê-PR&
Virmond-PR&
Vitorino-PR&
Wenceslau Braz-PR&
Xambrê-PR&
Abdon Batista-SC&
Abelardo Luz-SC&
Agrolândia-SC&
Agronômica-SC&
Água Doce-SC&
Águas de Chapecó-SC&
Águas Frias-SC&
Águas Mornas-SC&
Alfredo Wagner-SC&
Alto Bela Vista-SC&
Anchieta-SC&
Angelina-SC&
Anita Garibaldi-SC&
Anitápolis-SC&
Antônio Carlos-SC&
Apiúna-SC&
Arabutã-SC&
Araquari-SC&
Araranguá-SC&
Armazém-SC&
Arroio Trinta-SC&
Arvoredo-SC&
Ascurra-SC&
Atalanta-SC&
Aurora-SC&
Balneário Arroio do Silva-SC&
Balneário Barra do Sul-SC&
Balneário Camboriú-SC&
Balneário Gaivota-SC&
Balneário Piçarras-SC&
Bandeirante-SC&
Barra Bonita-SC&
Barra Velha-SC&
Bela Vista do Toldo-SC&
Belmonte-SC&
Benedito Novo-SC&
Biguaçu-SC&
Blumenau-SC&
Bocaina do Sul-SC&
Bom Jardim da Serra-SC&
Bom Jesus-SC&
Bom Jesus do Oeste-SC&
Bom Retiro-SC&
Bombinhas-SC&
Botuverá-SC&
Braço do Norte-SC&
Braço do Trombudo-SC&
Brunópolis-SC&
Brusque-SC&
Caçador-SC&
Caibi-SC&
Calmon-SC&
Camboriú-SC&
Campo Alegre-SC&
Campo Belo do Sul-SC&
Campo Erê-SC&
Campos Novos-SC&
Canelinha-SC&
Canoinhas-SC&
Capão Alto-SC&
Capinzal-SC&
Capivari de Baixo-SC&
Catanduvas-SC&
Caxambu do Sul-SC&
Celso Ramos-SC&
Cerro Negro-SC&
Chapadão do Lageado-SC&
Chapecó-SC&
Cocal do Sul-SC&
Concórdia-SC&
Cordilheira Alta-SC&
Coronel Freitas-SC&
Coronel Martins-SC&
Correia Pinto-SC&
Corupá-SC&
Criciúma-SC&
Cunha Porã-SC&
Cunhataí-SC&
Curitibanos-SC&
Descanso-SC&
Dionísio Cerqueira-SC&
Dona Emma-SC&
Doutor Pedrinho-SC&
Entre Rios-SC&
Ermo-SC&
Erval Velho-SC&
Faxinal dos Guedes-SC&
Flor do Sertão-SC&
Florianópolis-SC&
Formosa do Sul-SC&
Forquilhinha-SC&
Fraiburgo-SC&
Frei Rogério-SC&
Galvão-SC&
Garopaba-SC&
Garuva-SC&
Gaspar-SC&
Governador Celso Ramos-SC&
Grão Pará-SC&
Gravatal-SC&
Guabiruba-SC&
Guaraciaba-SC&
Guaramirim-SC&
Guarujá do Sul-SC&
Guatambú-SC&
Herval d'Oeste-SC&
Ibiam-SC&
Ibicaré-SC&
Ibirama-SC&
Içara-SC&
Ilhota-SC&
Imaruí-SC&
Imbituba-SC&
Imbuia-SC&
Indaial-SC&
Iomerê-SC&
Ipira-SC&
Iporã do Oeste-SC&
Ipuaçu-SC&
Ipumirim-SC&
Iraceminha-SC&
Irani-SC&
Irati-SC&
Irineópolis-SC&
Itá-SC&
Itaiópolis-SC&
Itajaí-SC&
Itapema-SC&
Itapiranga-SC&
Itapoá-SC&
Ituporanga-SC&
Jaborá-SC&
Jacinto Machado-SC&
Jaguaruna-SC&
Jaraguá do Sul-SC&
Jardinópolis-SC&
Joaçaba-SC&
Joinville-SC&
José Boiteux-SC&
Jupiá-SC&
Lacerdópolis-SC&
Lages-SC&
Laguna-SC&
Lajeado Grande-SC&
Laurentino-SC&
Lauro Muller-SC&
Lebon Régis-SC&
Leoberto Leal-SC&
Lindóia do Sul-SC&
Lontras-SC&
Luiz Alves-SC&
Luzerna-SC&
Macieira-SC&
Mafra-SC&
Major Gercino-SC&
Major Vieira-SC&
Maracajá-SC&
Maravilha-SC&
Marema-SC&
Massaranduba-SC&
Matos Costa-SC&
Meleiro-SC&
Mirim Doce-SC&
Modelo-SC&
Mondaí-SC&
Monte Carlo-SC&
Monte Castelo-SC&
Morro da Fumaça-SC&
Morro Grande-SC&
Navegantes-SC&
Nova Erechim-SC&
Nova Itaberaba-SC&
Nova Trento-SC&
Nova Veneza-SC&
Novo Horizonte-SC&
Orleans-SC&
Otacílio Costa-SC&
Ouro-SC&
Ouro Verde-SC&
Paial-SC&
Painel-SC&
Palhoça-SC&
Palma Sola-SC&
Palmeira-SC&
Palmitos-SC&
Papanduva-SC&
Paraíso-SC&
Passo de Torres-SC&
Passos Maia-SC&
Paulo Lopes-SC&
Pedras Grandes-SC&
Penha-SC&
Peritiba-SC&
Petrolândia-SC&
Pinhalzinho-SC&
Pinheiro Preto-SC&
Piratuba-SC&
Planalto Alegre-SC&
Pomerode-SC&
Ponte Alta-SC&
Ponte Alta do Norte-SC&
Ponte Serrada-SC&
Porto Belo-SC&
Porto União-SC&
Pouso Redondo-SC&
Praia Grande-SC&
Presidente Castello Branco-SC&
Presidente Getúlio-SC&
Presidente Nereu-SC&
Princesa-SC&
Quilombo-SC&
Rancho Queimado-SC&
Rio das Antas-SC&
Rio do Campo-SC&
Rio do Oeste-SC&
Rio do Sul-SC&
Rio dos Cedros-SC&
Rio Fortuna-SC&
Rio Negrinho-SC&
Rio Rufino-SC&
Riqueza-SC&
Rodeio-SC&
Romelândia-SC&
Salete-SC&
Saltinho-SC&
Salto Veloso-SC&
Sangão-SC&
Santa Cecília-SC&
Santa Helena-SC&
Santa Rosa de Lima-SC&
Santa Rosa do Sul-SC&
Santa Terezinha-SC&
Santa Terezinha do Progresso-SC&
Santiago do Sul-SC&
Santo Amaro da Imperatriz-SC&
São Bento do Sul-SC&
São Bernardino-SC&
São Bonifácio-SC&
São Carlos-SC&
São Cristovão do Sul-SC&
São Domingos-SC&
São Francisco do Sul-SC&
São João Batista-SC&
São João do Itaperiú-SC&
São João do Oeste-SC&
São João do Sul-SC&
São Joaquim-SC&
São José-SC&
São José do Cedro-SC&
São José do Cerrito-SC&
São Lourenço do Oeste-SC&
São Ludgero-SC&
São Martinho-SC&
São Miguel da Boa Vista-SC&
São Miguel do Oeste-SC&
São Pedro de Alcântara-SC&
Saudades-SC&
Schroeder-SC&
Seara-SC&
Serra Alta-SC&
Siderópolis-SC&
Sombrio-SC&
Sul Brasil-SC&
Taió-SC&
Tangará-SC&
Tigrinhos-SC&
Tijucas-SC&
Timbé do Sul-SC&
Timbó-SC&
Timbó Grande-SC&
Três Barras-SC&
Treviso-SC&
Treze de Maio-SC&
Treze Tílias-SC&
Trombudo Central-SC&
Tubarão-SC&
Tunápolis-SC&
Turvo-SC&
União do Oeste-SC&
Urubici-SC&
Urupema-SC&
Urussanga-SC&
Vargeão-SC&
Vargem-SC&
Vargem Bonita-SC&
Vidal Ramos-SC&
Videira-SC&
Vitor Meireles-SC&
Witmarsum-SC&
Xanxerê-SC&
Xavantina-SC&
Xaxim-SC&
Zortéa-SC&
Aceguá-RS&
Água Santa-RS&
Agudo-RS&
Ajuricaba-RS&
Alecrim-RS&
Alegrete-RS&
Alegria-RS&
Almirante Tamandaré do Sul-RS&
Alpestre-RS&
Alto Alegre-RS&
Alto Feliz-RS&
Alvorada-RS&
Amaral Ferrador-RS&
Ametista do Sul-RS&
André da Rocha-RS&
Anta Gorda-RS&
Antônio Prado-RS&
Arambaré-RS&
Araricá-RS&
Aratiba-RS&
Arroio do Meio-RS&
Arroio do Padre-RS&
Arroio do Sal-RS&
Arroio do Tigre-RS&
Arroio dos Ratos-RS&
Arroio Grande-RS&
Arvorezinha-RS&
Augusto Pestana-RS&
Áurea-RS&
Bagé-RS&
Balneário Pinhal-RS&
Barão-RS&
Barão de Cotegipe-RS&
Barão do Triunfo-RS&
Barra do Guarita-RS&
Barra do Quaraí-RS&
Barra do Ribeiro-RS&
Barra do Rio Azul-RS&
Barra Funda-RS&
Barracão-RS&
Barros Cassal-RS&
Benjamin Constant do Sul-RS&
Bento Gonçalves-RS&
Boa Vista das Missões-RS&
Boa Vista do Buricá-RS&
Boa Vista do Cadeado-RS&
Boa Vista do Incra-RS&
Boa Vista do Sul-RS&
Bom Jesus-RS&
Bom Princípio-RS&
Bom Progresso-RS&
Bom Retiro do Sul-RS&
Boqueirão do Leão-RS&
Bossoroca-RS&
Bozano-RS&
Braga-RS&
Brochier-RS&
Butiá-RS&
Caçapava do Sul-RS&
Cacequi-RS&
Cachoeira do Sul-RS&
Cachoeirinha-RS&
Cacique Doble-RS&
Caibaté-RS&
Caiçara-RS&
Camaquã-RS&
Camargo-RS&
Cambará do Sul-RS&
Campestre da Serra-RS&
Campina das Missões-RS&
Campinas do Sul-RS&
Campo Bom-RS&
Campo Novo-RS&
Campos Borges-RS&
Candelária-RS&
Cândido Godói-RS&
Candiota-RS&
Canela-RS&
Canguçu-RS&
Canoas-RS&
Canudos do Vale-RS&
Capão Bonito do Sul-RS&
Capão da Canoa-RS&
Capão do Cipó-RS&
Capão do Leão-RS&
Capela de Santana-RS&
Capitão-RS&
Capivari do Sul-RS&
Caraá-RS&
Carazinho-RS&
Carlos Barbosa-RS&
Carlos Gomes-RS&
Casca-RS&
Caseiros-RS&
Catuípe-RS&
Caxias do Sul-RS&
Centenário-RS&
Cerrito-RS&
Cerro Branco-RS&
Cerro Grande-RS&
Cerro Grande do Sul-RS&
Cerro Largo-RS&
Chapada-RS&
Charqueadas-RS&
Charrua-RS&
Chiapetta-RS&
Chuí-RS&
Chuvisca-RS&
Cidreira-RS&
Ciríaco-RS&
Colinas-RS&
Colorado-RS&
Condor-RS&
Constantina-RS&
Coqueiro Baixo-RS&
Coqueiros do Sul-RS&
Coronel Barros-RS&
Coronel Bicaco-RS&
Coronel Pilar-RS&
Cotiporã-RS&
Coxilha-RS&
Crissiumal-RS&
Cristal-RS&
Cristal do Sul-RS&
Cruz Alta-RS&
Cruzaltense-RS&
Cruzeiro do Sul-RS&
David Canabarro-RS&
Derrubadas-RS&
Dezesseis de Novembro-RS&
Dilermando de Aguiar-RS&
Dois Irmãos-RS&
Dois Irmãos das Missões-RS&
Dois Lajeados-RS&
Dom Feliciano-RS&
Dom Pedrito-RS&
Dom Pedro de Alcântara-RS&
Dona Francisca-RS&
Doutor Maurício Cardoso-RS&
Doutor Ricardo-RS&
Eldorado do Sul-RS&
Encantado-RS&
Encruzilhada do Sul-RS&
Engenho Velho-RS&
Entre Rios do Sul-RS&
Entre-Ijuís-RS&
Erebango-RS&
Erechim-RS&
Ernestina-RS&
Erval Grande-RS&
Erval Seco-RS&
Esmeralda-RS&
Esperança do Sul-RS&
Espumoso-RS&
Estação-RS&
Estância Velha-RS&
Esteio-RS&
Estrela-RS&
Estrela Velha-RS&
Eugênio de Castro-RS&
Fagundes Varela-RS&
Farroupilha-RS&
Faxinal do Soturno-RS&
Faxinalzinho-RS&
Fazenda Vilanova-RS&
Feliz-RS&
Flores da Cunha-RS&
Floriano Peixoto-RS&
Fontoura Xavier-RS&
Formigueiro-RS&
Forquetinha-RS&
Fortaleza dos Valos-RS&
Frederico Westphalen-RS&
Garibaldi-RS&
Garruchos-RS&
Gaurama-RS&
General Câmara-RS&
Gentil-RS&
Getúlio Vargas-RS&
Giruá-RS&
Glorinha-RS&
Gramado-RS&
Gramado dos Loureiros-RS&
Gramado Xavier-RS&
Gravataí-RS&
Guabiju-RS&
Guaíba-RS&
Guaporé-RS&
Guarani das Missões-RS&
Harmonia-RS&
Herval-RS&
Herveiras-RS&
Horizontina-RS&
Hulha Negra-RS&
Humaitá-RS&
Ibarama-RS&
Ibiaçá-RS&
Ibiraiaras-RS&
Ibirapuitã-RS&
Ibirubá-RS&
Igrejinha-RS&
Ijuí-RS&
Ilópolis-RS&
Imbé-RS&
Imigrante-RS&
Independência-RS&
Inhacorá-RS&
Ipê-RS&
Ipiranga do Sul-RS&
Iraí-RS&
Itaara-RS&
Itacurubi-RS&
Itapuca-RS&
Itaqui-RS&
Itati-RS&
Itatiba do Sul-RS&
Ivorá-RS&
Ivoti-RS&
Jaboticaba-RS&
Jacuizinho-RS&
Jacutinga-RS&
Jaguarão-RS&
Jaguari-RS&
Jaquirana-RS&
Jari-RS&
Jóia-RS&
Júlio de Castilhos-RS&
Lagoa Bonita do Sul-RS&
Lagoa dos Três Cantos-RS&
Lagoa Vermelha-RS&
Lagoão-RS&
Lajeado-RS&
Lajeado do Bugre-RS&
Lavras do Sul-RS&
Liberato Salzano-RS&
Lindolfo Collor-RS&
Linha Nova-RS&
Maçambara-RS&
Machadinho-RS&
Mampituba-RS&
Manoel Viana-RS&
Maquiné-RS&
Maratá-RS&
Marau-RS&
Marcelino Ramos-RS&
Mariana Pimentel-RS&
Mariano Moro-RS&
Marques de Souza-RS&
Mata-RS&
Mato Castelhano-RS&
Mato Leitão-RS&
Mato Queimado-RS&
Maximiliano de Almeida-RS&
Minas do Leão-RS&
Miraguaí-RS&
Montauri-RS&
Monte Alegre dos Campos-RS&
Monte Belo do Sul-RS&
Montenegro-RS&
Mormaço-RS&
Morrinhos do Sul-RS&
Morro Redondo-RS&
Morro Reuter-RS&
Mostardas-RS&
Muçum-RS&
Muitos Capões-RS&
Muliterno-RS&
Não-Me-Toque-RS&
Nicolau Vergueiro-RS&
Nonoai-RS&
Nova Alvorada-RS&
Nova Araçá-RS&
Nova Bassano-RS&
Nova Boa Vista-RS&
Nova Bréscia-RS&
Nova Candelária-RS&
Nova Esperança do Sul-RS&
Nova Hartz-RS&
Nova Pádua-RS&
Nova Palma-RS&
Nova Petrópolis-RS&
Nova Prata-RS&
Nova Ramada-RS&
Nova Roma do Sul-RS&
Nova Santa Rita-RS&
Novo Barreiro-RS&
Novo Cabrais-RS&
Novo Hamburgo-RS&
Novo Machado-RS&
Novo Tiradentes-RS&
Novo Xingu-RS&
Osório-RS&
Paim Filho-RS&
Palmares do Sul-RS&
Palmeira das Missões-RS&
Palmitinho-RS&
Panambi-RS&
Pantano Grande-RS&
Paraí-RS&
Paraíso do Sul-RS&
Pareci Novo-RS&
Parobé-RS&
Passa Sete-RS&
Passo do Sobrado-RS&
Passo Fundo-RS&
Paulo Bento-RS&
Paverama-RS&
Pedras Altas-RS&
Pedro Osório-RS&
Pejuçara-RS&
Pelotas-RS&
Picada Café-RS&
Pinhal-RS&
Pinhal da Serra-RS&
Pinhal Grande-RS&
Pinheirinho do Vale-RS&
Pinheiro Machado-RS&
Pirapó-RS&
Piratini-RS&
Planalto-RS&
Poço das Antas-RS&
Pontão-RS&
Ponte Preta-RS&
Portão-RS&
Porto Alegre-RS&
Porto Lucena-RS&
Porto Mauá-RS&
Porto Vera Cruz-RS&
Porto Xavier-RS&
Pouso Novo-RS&
Presidente Lucena-RS&
Progresso-RS&
Protásio Alves-RS&
Putinga-RS&
Quaraí-RS&
Quatro Irmãos-RS&
Quevedos-RS&
Quinze de Novembro-RS&
Redentora-RS&
Relvado-RS&
Restinga Seca-RS&
Rio dos Índios-RS&
Rio Grande-RS&
Rio Pardo-RS&
Riozinho-RS&
Roca Sales-RS&
Rodeio Bonito-RS&
Rolador-RS&
Rolante-RS&
Ronda Alta-RS&
Rondinha-RS&
Roque Gonzales-RS&
Rosário do Sul-RS&
Sagrada Família-RS&
Saldanha Marinho-RS&
Salto do Jacuí-RS&
Salvador das Missões-RS&
Salvador do Sul-RS&
Sananduva-RS&
Santa Bárbara do Sul-RS&
Santa Cecília do Sul-RS&
Santa Clara do Sul-RS&
Santa Cruz do Sul-RS&
Santa Margarida do Sul-RS&
Santa Maria-RS&
Santa Maria do Herval-RS&
Santa Rosa-RS&
Santa Tereza-RS&
Santa Vitória do Palmar-RS&
Santana da Boa Vista-RS&
Santana do Livramento-RS&
Santiago-RS&
Santo Ângelo-RS&
Santo Antônio da Patrulha-RS&
Santo Antônio das Missões-RS&
Santo Antônio do Palma-RS&
Santo Antônio do Planalto-RS&
Santo Augusto-RS&
Santo Cristo-RS&
Santo Expedito do Sul-RS&
São Borja-RS&
São Domingos do Sul-RS&
São Francisco de Assis-RS&
São Francisco de Paula-RS&
São Gabriel-RS&
São Jerônimo-RS&
São João da Urtiga-RS&
São João do Polêsine-RS&
São Jorge-RS&
São José das Missões-RS&
São José do Herval-RS&
São José do Hortêncio-RS&
São José do Inhacorá-RS&
São José do Norte-RS&
São José do Ouro-RS&
São José do Sul-RS&
São José dos Ausentes-RS&
São Leopoldo-RS&
São Lourenço do Sul-RS&
São Luiz Gonzaga-RS&
São Marcos-RS&
São Martinho-RS&
São Martinho da Serra-RS&
São Miguel das Missões-RS&
São Nicolau-RS&
São Paulo das Missões-RS&
São Pedro da Serra-RS&
São Pedro das Missões-RS&
São Pedro do Butiá-RS&
São Pedro do Sul-RS&
São Sebastião do Caí-RS&
São Sepé-RS&
São Valentim-RS&
São Valentim do Sul-RS&
São Valério do Sul-RS&
São Vendelino-RS&
São Vicente do Sul-RS&
Sapiranga-RS&
Sapucaia do Sul-RS&
Sarandi-RS&
Seberi-RS&
Sede Nova-RS&
Segredo-RS&
Selbach-RS&
Senador Salgado Filho-RS&
Sentinela do Sul-RS&
Serafina Corrêa-RS&
Sério-RS&
Sertão-RS&
Sertão Santana-RS&
Sete de Setembro-RS&
Severiano de Almeida-RS&
Silveira Martins-RS&
Sinimbu-RS&
Sobradinho-RS&
Soledade-RS&
Tabaí-RS&
Tapejara-RS&
Tapera-RS&
Tapes-RS&
Taquara-RS&
Taquari-RS&
Taquaruçu do Sul-RS&
Tavares-RS&
Tenente Portela-RS&
Terra de Areia-RS&
Teutônia-RS&
Tio Hugo-RS&
Tiradentes do Sul-RS&
Toropi-RS&
Torres-RS&
Tramandaí-RS&
Travesseiro-RS&
Três Arroios-RS&
Três Cachoeiras-RS&
Três Coroas-RS&
Três de Maio-RS&
Três Forquilhas-RS&
Três Palmeiras-RS&
Três Passos-RS&
Trindade do Sul-RS&
Triunfo-RS&
Tucunduva-RS&
Tunas-RS&
Tupanci do Sul-RS&
Tupanciretã-RS&
Tupandi-RS&
Tuparendi-RS&
Turuçu-RS&
Ubiretama-RS&
União da Serra-RS&
Unistalda-RS&
Uruguaiana-RS&
Vacaria-RS&
Vale do Sol-RS&
Vale Real-RS&
Vale Verde-RS&
Vanini-RS&
Venâncio Aires-RS&
Vera Cruz-RS&
Veranópolis-RS&
Vespasiano Correa-RS&
Viadutos-RS&
Viamão-RS&
Vicente Dutra-RS&
Victor Graeff-RS&
Vila Flores-RS&
Vila Lângaro-RS&
Vila Maria-RS&
Vila Nova do Sul-RS&
Vista Alegre-RS&
Vista Alegre do Prata-RS&
Vista Gaúcha-RS&
Vitória das Missões-RS&
Westfalia-RS&
Xangri-lá-RS&
Água Clara-MS&
Alcinópolis-MS&
Amambaí-MS&
Anastácio-MS&
Anaurilândia-MS&
Angélica-MS&
Antônio João-MS&
Aparecida do Taboado-MS&
Aquidauana-MS&
Aral Moreira-MS&
Bandeirantes-MS&
Bataguassu-MS&
Batayporã-MS&
Bela Vista-MS&
Bodoquena-MS&
Bonito-MS&
Brasilândia-MS&
Caarapó-MS&
Camapuã-MS&
Campo Grande-MS&
Caracol-MS&
Cassilândia-MS&
Chapadão do Sul-MS&
Corguinho-MS&
Coronel Sapucaia-MS&
Corumbá-MS&
Costa Rica-MS&
Coxim-MS&
Deodápolis-MS&
Dois Irmãos do Buriti-MS&
Douradina-MS&
Dourados-MS&
Eldorado-MS&
Fátima do Sul-MS&
Figueirão-MS&
Glória de Dourados-MS&
Guia Lopes da Laguna-MS&
Iguatemi-MS&
Inocência-MS&
Itaporã-MS&
Itaquiraí-MS&
Ivinhema-MS&
Japorã-MS&
Jaraguari-MS&
Jardim-MS&
Jateí-MS&
Juti-MS&
Ladário-MS&
Laguna Carapã-MS&
Maracaju-MS&
Miranda-MS&
Mundo Novo-MS&
Naviraí-MS&
Nioaque-MS&
Nova Alvorada do Sul-MS&
Nova Andradina-MS&
Novo Horizonte do Sul-MS&
Paranaíba-MS&
Paranhos-MS&
Pedro Gomes-MS&
Ponta Porã-MS&
Porto Murtinho-MS&
Ribas do Rio Pardo-MS&
Rio Brilhante-MS&
Rio Negro-MS&
Rio Verde de Mato Grosso-MS&
Rochedo-MS&
Santa Rita do Pardo-MS&
São Gabriel do Oeste-MS&
Selvíria-MS&
Sete Quedas-MS&
Sidrolândia-MS&
Sonora-MS&
Tacuru-MS&
Taquarussu-MS&
Terenos-MS&
Três Lagoas-MS&
Vicentina-MS&
Acorizal-MT&
Água Boa-MT&
Alta Floresta-MT&
Alto Araguaia-MT&
Alto Boa Vista-MT&
Alto Garças-MT&
Alto Paraguai-MT&
Alto Taquari-MT&
Apiacás-MT&
Araguaiana-MT&
Araguainha-MT&
Araputanga-MT&
Arenápolis-MT&
Aripuanã-MT&
Barão de Melgaço-MT&
Barra do Bugres-MT&
Barra do Garças-MT&
Bom Jesus do Araguaia-MT&
Brasnorte-MT&
Cáceres-MT&
Campinápolis-MT&
Campo Novo do Parecis-MT&
Campo Verde-MT&
Campos de Júlio-MT&
Canabrava do Norte-MT&
Canarana-MT&
Carlinda-MT&
Castanheira-MT&
Chapada dos Guimarães-MT&
Cláudia-MT&
Cocalinho-MT&
Colíder-MT&
Colniza-MT&
Comodoro-MT&
Confresa-MT&
Conquista D'Oeste-MT&
Cotriguaçu-MT&
Cuiabá-MT&
Curvelândia-MT&
Denise-MT&
Diamantino-MT&
Dom Aquino-MT&
Feliz Natal-MT&
Figueirópolis D'Oeste-MT&
Gaúcha do Norte-MT&
General Carneiro-MT&
Glória D'Oeste-MT&
Guarantã do Norte-MT&
Guiratinga-MT&
Indiavaí-MT&
Ipiranga do Norte-MT&
Itanhangá-MT&
Itaúba-MT&
Itiquira-MT&
Jaciara-MT&
Jangada-MT&
Jauru-MT&
Juara-MT&
Juína-MT&
Juruena-MT&
Juscimeira-MT&
Lambari D'Oeste-MT&
Lucas do Rio Verde-MT&
Luciára-MT&
Marcelândia-MT&
Matupá-MT&
Mirassol d'Oeste-MT&
Nobres-MT&
Nortelândia-MT&
Nossa Senhora do Livramento-MT&
Nova Bandeirantes-MT&
Nova Brasilândia-MT&
Nova Canaã do Norte-MT&
Nova Guarita-MT&
Nova Lacerda-MT&
Nova Marilândia-MT&
Nova Maringá-MT&
Nova Monte Verde-MT&
Nova Mutum-MT&
Nova Nazaré-MT&
Nova Olímpia-MT&
Nova Santa Helena-MT&
Nova Ubiratã-MT&
Nova Xavantina-MT&
Novo Horizonte do Norte-MT&
Novo Mundo-MT&
Novo Santo Antônio-MT&
Novo São Joaquim-MT&
Paranaíta-MT&
Paranatinga-MT&
Pedra Preta-MT&
Peixoto de Azevedo-MT&
Planalto da Serra-MT&
Poconé-MT&
Pontal do Araguaia-MT&
Ponte Branca-MT&
Pontes e Lacerda-MT&
Porto Alegre do Norte-MT&
Porto dos Gaúchos-MT&
Porto Esperidião-MT&
Porto Estrela-MT&
Poxoréo-MT&
Primavera do Leste-MT&
Querência-MT&
Reserva do Cabaçal-MT&
Ribeirão Cascalheira-MT&
Ribeirãozinho-MT&
Rio Branco-MT&
Rondolândia-MT&
Rondonópolis-MT&
Rosário Oeste-MT&
Salto do Céu-MT&
Santa Carmem-MT&
Santa Cruz do Xingu-MT&
Santa Rita do Trivelato-MT&
Santa Terezinha-MT&
Santo Afonso-MT&
Santo Antônio do Leste-MT&
Santo Antônio do Leverger-MT&
São Félix do Araguaia-MT&
São José do Povo-MT&
São José do Rio Claro-MT&
São José do Xingu-MT&
São José dos Quatro Marcos-MT&
São Pedro da Cipa-MT&
Sapezal-MT&
Serra Nova Dourada-MT&
Sinop-MT&
Sorriso-MT&
Tabaporã-MT&
Tangará da Serra-MT&
Tapurah-MT&
Terra Nova do Norte-MT&
Tesouro-MT&
Torixoréu-MT&
União do Sul-MT&
Vale de São Domingos-MT&
Várzea Grande-MT&
Vera-MT&
Vila Bela da Santíssima Trindade-MT&
Vila Rica-MT&
Abadia de Goiás-GO&
Abadiânia-GO&
Acreúna-GO&
Adelândia-GO&
Água Fria de Goiás-GO&
Água Limpa-GO&
Águas Lindas de Goiás-GO&
Alexânia-GO&
Aloândia-GO&
Alto Horizonte-GO&
Alto Paraíso de Goiás-GO&
Alvorada do Norte-GO&
Amaralina-GO&
Americano do Brasil-GO&
Amorinópolis-GO&
Anápolis-GO&
Anhanguera-GO&
Anicuns-GO&
Aparecida de Goiânia-GO&
Aparecida do Rio Doce-GO&
Aporé-GO&
Araçu-GO&
Aragarças-GO&
Aragoiânia-GO&
Araguapaz-GO&
Arenópolis-GO&
Aruanã-GO&
Aurilândia-GO&
Avelinópolis-GO&
Baliza-GO&
Barro Alto-GO&
Bela Vista de Goiás-GO&
Bom Jardim de Goiás-GO&
Bom Jesus de Goiás-GO&
Bonfinópolis-GO&
Bonópolis-GO&
Brazabrantes-GO&
Britânia-GO&
Buriti Alegre-GO&
Buriti de Goiás-GO&
Buritinópolis-GO&
Cabeceiras-GO&
Cachoeira Alta-GO&
Cachoeira de Goiás-GO&
Cachoeira Dourada-GO&
Caçu-GO&
Caiapônia-GO&
Caldas Novas-GO&
Caldazinha-GO&
Campestre de Goiás-GO&
Campinaçu-GO&
Campinorte-GO&
Campo Alegre de Goiás-GO&
Campo Limpo de Goiás-GO&
Campos Belos-GO&
Campos Verdes-GO&
Carmo do Rio Verde-GO&
Castelândia-GO&
Catalão-GO&
Caturaí-GO&
Cavalcante-GO&
Ceres-GO&
Cezarina-GO&
Chapadão do Céu-GO&
Cidade Ocidental-GO&
Cocalzinho de Goiás-GO&
Colinas do Sul-GO&
Córrego do Ouro-GO&
Corumbá de Goiás-GO&
Corumbaíba-GO&
Cristalina-GO&
Cristianópolis-GO&
Crixás-GO&
Cromínia-GO&
Cumari-GO&
Damianópolis-GO&
Damolândia-GO&
Davinópolis-GO&
Diorama-GO&
Divinópolis de Goiás-GO&
Doverlândia-GO&
Edealina-GO&
Edéia-GO&
Estrela do Norte-GO&
Faina-GO&
Fazenda Nova-GO&
Firminópolis-GO&
Flores de Goiás-GO&
Formosa-GO&
Formoso-GO&
Gameleira de Goiás-GO&
Goianápolis-GO&
Goiandira-GO&
Goianésia-GO&
Goiânia-GO&
Goianira-GO&
Goiás-GO&
Goiatuba-GO&
Gouvelândia-GO&
Guapó-GO&
Guaraíta-GO&
Guarani de Goiás-GO&
Guarinos-GO&
Heitoraí-GO&
Hidrolândia-GO&
Hidrolina-GO&
Iaciara-GO&
Inaciolândia-GO&
Indiara-GO&
Inhumas-GO&
Ipameri-GO&
Ipiranga de Goiás-GO&
Iporá-GO&
Israelândia-GO&
Itaberaí-GO&
Itaguari-GO&
Itaguaru-GO&
Itajá-GO&
Itapaci-GO&
Itapirapuã-GO&
Itapuranga-GO&
Itarumã-GO&
Itauçu-GO&
Itumbiara-GO&
Ivolândia-GO&
Jandaia-GO&
Jaraguá-GO&
Jataí-GO&
Jaupaci-GO&
Jesúpolis-GO&
Joviânia-GO&
Jussara-GO&
Lagoa Santa-GO&
Leopoldo de Bulhões-GO&
Luziânia-GO&
Mairipotaba-GO&
Mambaí-GO&
Mara Rosa-GO&
Marzagão-GO&
Matrinchã-GO&
Maurilândia-GO&
Mimoso de Goiás-GO&
Minaçu-GO&
Mineiros-GO&
Moiporá-GO&
Monte Alegre de Goiás-GO&
Montes Claros de Goiás-GO&
Montividiu-GO&
Montividiu do Norte-GO&
Morrinhos-GO&
Morro Agudo de Goiás-GO&
Mossâmedes-GO&
Mozarlândia-GO&
Mundo Novo-GO&
Mutunópolis-GO&
Nazário-GO&
Nerópolis-GO&
Niquelândia-GO&
Nova América-GO&
Nova Aurora-GO&
Nova Crixás-GO&
Nova Glória-GO&
Nova Iguaçu de Goiás-GO&
Nova Roma-GO&
Nova Veneza-GO&
Novo Brasil-GO&
Novo Gama-GO&
Novo Planalto-GO&
Orizona-GO&
Ouro Verde de Goiás-GO&
Ouvidor-GO&
Padre Bernardo-GO&
Palestina de Goiás-GO&
Palmeiras de Goiás-GO&
Palmelo-GO&
Palminópolis-GO&
Panamá-GO&
Paranaiguara-GO&
Paraúna-GO&
Perolândia-GO&
Petrolina de Goiás-GO&
Pilar de Goiás-GO&
Piracanjuba-GO&
Piranhas-GO&
Pirenópolis-GO&
Pires do Rio-GO&
Planaltina-GO&
Pontalina-GO&
Porangatu-GO&
Porteirão-GO&
Portelândia-GO&
Posse-GO&
Professor Jamil-GO&
Quirinópolis-GO&
Rialma-GO&
Rianápolis-GO&
Rio Quente-GO&
Rio Verde-GO&
Rubiataba-GO&
Sanclerlândia-GO&
Santa Bárbara de Goiás-GO&
Santa Cruz de Goiás-GO&
Santa Fé de Goiás-GO&
Santa Helena de Goiás-GO&
Santa Isabel-GO&
Santa Rita do Araguaia-GO&
Santa Rita do Novo Destino-GO&
Santa Rosa de Goiás-GO&
Santa Tereza de Goiás-GO&
Santa Terezinha de Goiás-GO&
Santo Antônio da Barra-GO&
Santo Antônio de Goiás-GO&
Santo Antônio do Descoberto-GO&
São Domingos-GO&
São Francisco de Goiás-GO&
São João da Paraúna-GO&
São João d'Aliança-GO&
São Luís de Montes Belos-GO&
São Luíz do Norte-GO&
São Miguel do Araguaia-GO&
São Miguel do Passa Quatro-GO&
São Patrício-GO&
São Simão-GO&
Senador Canedo-GO&
Serranópolis-GO&
Silvânia-GO&
Simolândia-GO&
Sítio d'Abadia-GO&
Taquaral de Goiás-GO&
Teresina de Goiás-GO&
Terezópolis de Goiás-GO&
Três Ranchos-GO&
Trindade-GO&
Trombas-GO&
Turvânia-GO&
Turvelândia-GO&
Uirapuru-GO&
Uruaçu-GO&
Uruana-GO&
Urutaí-GO&
Valparaíso de Goiás-GO&
Varjão-GO&
Vianópolis-GO&
Vicentinópolis-GO&
Vila Boa-GO&
Vila Propício-GO&
Brasília-DF&
'''
city = list(city)
for i in range(len(city)):
    city[i] = city[i].rstrip('\n')
city = ''.join(city)
city = city.split('&')
