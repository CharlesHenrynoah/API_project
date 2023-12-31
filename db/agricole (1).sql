PGDMP  4                 	    {           agricole    16.0    16.0 ;    Y           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            Z           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            [           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            \           1262    16473    agricole    DATABASE     j   CREATE DATABASE agricole WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
    DROP DATABASE agricole;
                postgres    false            �            1259    16582    CULTURE    TABLE     �   CREATE TABLE public."CULTURE" (
    "IDENTIFIANT_CULTURE" smallint NOT NULL,
    "NO_PARCELLE" smallint,
    "CODE_PRODUCTION" smallint,
    "DATE_DEBUT" date,
    "DATE_FIN" date,
    "QTE_RECOLTEE" numeric
);
    DROP TABLE public."CULTURE";
       public         heap    postgres    false            �            1259    16581    CULTURE_IDENTIFIANT_CULTURE_seq    SEQUENCE     �   CREATE SEQUENCE public."CULTURE_IDENTIFIANT_CULTURE_seq"
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public."CULTURE_IDENTIFIANT_CULTURE_seq";
       public          postgres    false    216            ]           0    0    CULTURE_IDENTIFIANT_CULTURE_seq    SEQUENCE OWNED BY     i   ALTER SEQUENCE public."CULTURE_IDENTIFIANT_CULTURE_seq" OWNED BY public."CULTURE"."IDENTIFIANT_CULTURE";
          public          postgres    false    215            �            1259    16618    DATE    TABLE     9   CREATE TABLE public."DATE" (
    "DATE" date NOT NULL
);
    DROP TABLE public."DATE";
       public         heap    postgres    false            �            1259    16637    ELEMENT_CHIMIQUES    TABLE     �   CREATE TABLE public."ELEMENT_CHIMIQUES" (
    "CODE_ELEMENT" character(5) NOT NULL,
    "UN" character(20),
    "LIBELLE_ELEMENT" character(20)
);
 '   DROP TABLE public."ELEMENT_CHIMIQUES";
       public         heap    postgres    false            �            1259    16624    ENGRAIS    TABLE        CREATE TABLE public."ENGRAIS" (
    "ID_ENGRAIS" smallint NOT NULL,
    "UN" character(20),
    "NOM_ENGRAIS" character(20)
);
    DROP TABLE public."ENGRAIS";
       public         heap    postgres    false            �            1259    16623    ENGRAIS_ID_ENGRAIS_seq    SEQUENCE     �   CREATE SEQUENCE public."ENGRAIS_ID_ENGRAIS_seq"
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public."ENGRAIS_ID_ENGRAIS_seq";
       public          postgres    false    225            ^           0    0    ENGRAIS_ID_ENGRAIS_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public."ENGRAIS_ID_ENGRAIS_seq" OWNED BY public."ENGRAIS"."ID_ENGRAIS";
          public          postgres    false    224            �            1259    16611    EPANDRE    TABLE     �   CREATE TABLE public."EPANDRE" (
    "ID_ENGRAIS" smallint NOT NULL,
    "NO_PARCELLE" smallint NOT NULL,
    "DATE" date NOT NULL,
    "QTE_EPANDUE" numeric
);
    DROP TABLE public."EPANDRE";
       public         heap    postgres    false            �            1259    16692    LOG    TABLE     �   CREATE TABLE public."LOG" (
    "APP_GET" integer,
    "APP_POST" integer,
    "APP_DELETE" integer,
    "APP_PATCH" integer
);
    DROP TABLE public."LOG";
       public         heap    postgres    false            �            1259    16591    PARCELLE    TABLE     �   CREATE TABLE public."PARCELLE" (
    "NO_PARCELLE" smallint NOT NULL,
    "SURFACE" numeric,
    "NOM_PARCELLE" character(20),
    "COORDONNEES" character(20)
);
    DROP TABLE public."PARCELLE";
       public         heap    postgres    false            �            1259    16590    PARCELLE_NO_PARCELLE_seq    SEQUENCE     �   CREATE SEQUENCE public."PARCELLE_NO_PARCELLE_seq"
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public."PARCELLE_NO_PARCELLE_seq";
       public          postgres    false    218            _           0    0    PARCELLE_NO_PARCELLE_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public."PARCELLE_NO_PARCELLE_seq" OWNED BY public."PARCELLE"."NO_PARCELLE";
          public          postgres    false    217            �            1259    16630    POSSEDER    TABLE     �   CREATE TABLE public."POSSEDER" (
    "ID_ENGRAIS" smallint NOT NULL,
    "CODE_ELEMENT" character(5) NOT NULL,
    "VALEUR" numeric
);
    DROP TABLE public."POSSEDER";
       public         heap    postgres    false            �            1259    16600 
   PRODUCTION    TABLE     �   CREATE TABLE public."PRODUCTION" (
    "CODE_PRODUCTION" smallint NOT NULL,
    "UN" character(20),
    "NOM_PRODUCTION" character(20)
);
     DROP TABLE public."PRODUCTION";
       public         heap    postgres    false            �            1259    16599    PRODUCTION_CODE_PRODUCTION_seq    SEQUENCE     �   CREATE SEQUENCE public."PRODUCTION_CODE_PRODUCTION_seq"
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public."PRODUCTION_CODE_PRODUCTION_seq";
       public          postgres    false    220            `           0    0    PRODUCTION_CODE_PRODUCTION_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public."PRODUCTION_CODE_PRODUCTION_seq" OWNED BY public."PRODUCTION"."CODE_PRODUCTION";
          public          postgres    false    219            �            1259    16606    UNITE    TABLE     A   CREATE TABLE public."UNITE" (
    "UN" character(20) NOT NULL
);
    DROP TABLE public."UNITE";
       public         heap    postgres    false            �           2604    16585    CULTURE IDENTIFIANT_CULTURE    DEFAULT     �   ALTER TABLE ONLY public."CULTURE" ALTER COLUMN "IDENTIFIANT_CULTURE" SET DEFAULT nextval('public."CULTURE_IDENTIFIANT_CULTURE_seq"'::regclass);
 N   ALTER TABLE public."CULTURE" ALTER COLUMN "IDENTIFIANT_CULTURE" DROP DEFAULT;
       public          postgres    false    215    216    216            �           2604    16627    ENGRAIS ID_ENGRAIS    DEFAULT     ~   ALTER TABLE ONLY public."ENGRAIS" ALTER COLUMN "ID_ENGRAIS" SET DEFAULT nextval('public."ENGRAIS_ID_ENGRAIS_seq"'::regclass);
 E   ALTER TABLE public."ENGRAIS" ALTER COLUMN "ID_ENGRAIS" DROP DEFAULT;
       public          postgres    false    224    225    225            �           2604    16594    PARCELLE NO_PARCELLE    DEFAULT     �   ALTER TABLE ONLY public."PARCELLE" ALTER COLUMN "NO_PARCELLE" SET DEFAULT nextval('public."PARCELLE_NO_PARCELLE_seq"'::regclass);
 G   ALTER TABLE public."PARCELLE" ALTER COLUMN "NO_PARCELLE" DROP DEFAULT;
       public          postgres    false    218    217    218            �           2604    16603    PRODUCTION CODE_PRODUCTION    DEFAULT     �   ALTER TABLE ONLY public."PRODUCTION" ALTER COLUMN "CODE_PRODUCTION" SET DEFAULT nextval('public."PRODUCTION_CODE_PRODUCTION_seq"'::regclass);
 M   ALTER TABLE public."PRODUCTION" ALTER COLUMN "CODE_PRODUCTION" DROP DEFAULT;
       public          postgres    false    220    219    220            J          0    16582    CULTURE 
   TABLE DATA           �   COPY public."CULTURE" ("IDENTIFIANT_CULTURE", "NO_PARCELLE", "CODE_PRODUCTION", "DATE_DEBUT", "DATE_FIN", "QTE_RECOLTEE") FROM stdin;
    public          postgres    false    216   gH       Q          0    16618    DATE 
   TABLE DATA           (   COPY public."DATE" ("DATE") FROM stdin;
    public          postgres    false    223   �H       U          0    16637    ELEMENT_CHIMIQUES 
   TABLE DATA           V   COPY public."ELEMENT_CHIMIQUES" ("CODE_ELEMENT", "UN", "LIBELLE_ELEMENT") FROM stdin;
    public          postgres    false    227   �H       S          0    16624    ENGRAIS 
   TABLE DATA           F   COPY public."ENGRAIS" ("ID_ENGRAIS", "UN", "NOM_ENGRAIS") FROM stdin;
    public          postgres    false    225   �H       P          0    16611    EPANDRE 
   TABLE DATA           W   COPY public."EPANDRE" ("ID_ENGRAIS", "NO_PARCELLE", "DATE", "QTE_EPANDUE") FROM stdin;
    public          postgres    false    222   �H       V          0    16692    LOG 
   TABLE DATA           Q   COPY public."LOG" ("APP_GET", "APP_POST", "APP_DELETE", "APP_PATCH") FROM stdin;
    public          postgres    false    228   �H       L          0    16591    PARCELLE 
   TABLE DATA           ]   COPY public."PARCELLE" ("NO_PARCELLE", "SURFACE", "NOM_PARCELLE", "COORDONNEES") FROM stdin;
    public          postgres    false    218   I       T          0    16630    POSSEDER 
   TABLE DATA           L   COPY public."POSSEDER" ("ID_ENGRAIS", "CODE_ELEMENT", "VALEUR") FROM stdin;
    public          postgres    false    226   2I       N          0    16600 
   PRODUCTION 
   TABLE DATA           Q   COPY public."PRODUCTION" ("CODE_PRODUCTION", "UN", "NOM_PRODUCTION") FROM stdin;
    public          postgres    false    220   OI       O          0    16606    UNITE 
   TABLE DATA           '   COPY public."UNITE" ("UN") FROM stdin;
    public          postgres    false    221   lI       a           0    0    CULTURE_IDENTIFIANT_CULTURE_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public."CULTURE_IDENTIFIANT_CULTURE_seq"', 1, false);
          public          postgres    false    215            b           0    0    ENGRAIS_ID_ENGRAIS_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public."ENGRAIS_ID_ENGRAIS_seq"', 1, false);
          public          postgres    false    224            c           0    0    PARCELLE_NO_PARCELLE_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public."PARCELLE_NO_PARCELLE_seq"', 1, false);
          public          postgres    false    217            d           0    0    PRODUCTION_CODE_PRODUCTION_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public."PRODUCTION_CODE_PRODUCTION_seq"', 1, false);
          public          postgres    false    219            �           2606    16589    CULTURE CULTURE_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public."CULTURE"
    ADD CONSTRAINT "CULTURE_pkey" PRIMARY KEY ("IDENTIFIANT_CULTURE");
 B   ALTER TABLE ONLY public."CULTURE" DROP CONSTRAINT "CULTURE_pkey";
       public            postgres    false    216            �           2606    16622    DATE DATE_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public."DATE"
    ADD CONSTRAINT "DATE_pkey" PRIMARY KEY ("DATE");
 <   ALTER TABLE ONLY public."DATE" DROP CONSTRAINT "DATE_pkey";
       public            postgres    false    223            �           2606    16696 (   ELEMENT_CHIMIQUES ELEMENT_CHIMIQUES_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public."ELEMENT_CHIMIQUES"
    ADD CONSTRAINT "ELEMENT_CHIMIQUES_pkey" PRIMARY KEY ("CODE_ELEMENT");
 V   ALTER TABLE ONLY public."ELEMENT_CHIMIQUES" DROP CONSTRAINT "ELEMENT_CHIMIQUES_pkey";
       public            postgres    false    227            �           2606    16629    ENGRAIS ENGRAIS_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public."ENGRAIS"
    ADD CONSTRAINT "ENGRAIS_pkey" PRIMARY KEY ("ID_ENGRAIS");
 B   ALTER TABLE ONLY public."ENGRAIS" DROP CONSTRAINT "ENGRAIS_pkey";
       public            postgres    false    225            �           2606    16617    EPANDRE EPANDRE_pkey 
   CONSTRAINT     w   ALTER TABLE ONLY public."EPANDRE"
    ADD CONSTRAINT "EPANDRE_pkey" PRIMARY KEY ("ID_ENGRAIS", "NO_PARCELLE", "DATE");
 B   ALTER TABLE ONLY public."EPANDRE" DROP CONSTRAINT "EPANDRE_pkey";
       public            postgres    false    222    222    222            �           2606    16598    PARCELLE PARCELLE_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public."PARCELLE"
    ADD CONSTRAINT "PARCELLE_pkey" PRIMARY KEY ("NO_PARCELLE");
 D   ALTER TABLE ONLY public."PARCELLE" DROP CONSTRAINT "PARCELLE_pkey";
       public            postgres    false    218            �           2606    16636    POSSEDER POSSEDER_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public."POSSEDER"
    ADD CONSTRAINT "POSSEDER_pkey" PRIMARY KEY ("ID_ENGRAIS", "CODE_ELEMENT");
 D   ALTER TABLE ONLY public."POSSEDER" DROP CONSTRAINT "POSSEDER_pkey";
       public            postgres    false    226    226            �           2606    16605    PRODUCTION PRODUCTION_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public."PRODUCTION"
    ADD CONSTRAINT "PRODUCTION_pkey" PRIMARY KEY ("CODE_PRODUCTION");
 H   ALTER TABLE ONLY public."PRODUCTION" DROP CONSTRAINT "PRODUCTION_pkey";
       public            postgres    false    220            �           2606    16610    UNITE UNITE_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public."UNITE"
    ADD CONSTRAINT "UNITE_pkey" PRIMARY KEY ("UN");
 >   ALTER TABLE ONLY public."UNITE" DROP CONSTRAINT "UNITE_pkey";
       public            postgres    false    221            �           2606    16687 =   CULTURE CULTURE_CODE_PRODUCTION -> PRODUCTION_CODE_PRODUCTION    FK CONSTRAINT     �   ALTER TABLE ONLY public."CULTURE"
    ADD CONSTRAINT "CULTURE_CODE_PRODUCTION -> PRODUCTION_CODE_PRODUCTION" FOREIGN KEY ("CODE_PRODUCTION") REFERENCES public."PRODUCTION"("CODE_PRODUCTION") NOT VALID;
 k   ALTER TABLE ONLY public."CULTURE" DROP CONSTRAINT "CULTURE_CODE_PRODUCTION -> PRODUCTION_CODE_PRODUCTION";
       public          postgres    false    216    3491    220            �           2606    16642 3   CULTURE CULTURE_NO_PARCELLE -> PARCELLE_NO_PARCELLE    FK CONSTRAINT     �   ALTER TABLE ONLY public."CULTURE"
    ADD CONSTRAINT "CULTURE_NO_PARCELLE -> PARCELLE_NO_PARCELLE" FOREIGN KEY ("NO_PARCELLE") REFERENCES public."PARCELLE"("NO_PARCELLE") NOT VALID;
 a   ALTER TABLE ONLY public."CULTURE" DROP CONSTRAINT "CULTURE_NO_PARCELLE -> PARCELLE_NO_PARCELLE";
       public          postgres    false    216    3489    218            �           2606    16682 2   ELEMENT_CHIMIQUES ELEMENT_CHIMIQUES_UN -> UNITE_UN    FK CONSTRAINT     �   ALTER TABLE ONLY public."ELEMENT_CHIMIQUES"
    ADD CONSTRAINT "ELEMENT_CHIMIQUES_UN -> UNITE_UN" FOREIGN KEY ("UN") REFERENCES public."UNITE"("UN") NOT VALID;
 `   ALTER TABLE ONLY public."ELEMENT_CHIMIQUES" DROP CONSTRAINT "ELEMENT_CHIMIQUES_UN -> UNITE_UN";
       public          postgres    false    227    221    3493            �           2606    16662    ENGRAIS ENGRAIS_UN -> UNITE_UN    FK CONSTRAINT     �   ALTER TABLE ONLY public."ENGRAIS"
    ADD CONSTRAINT "ENGRAIS_UN -> UNITE_UN" FOREIGN KEY ("UN") REFERENCES public."UNITE"("UN") NOT VALID;
 L   ALTER TABLE ONLY public."ENGRAIS" DROP CONSTRAINT "ENGRAIS_UN -> UNITE_UN";
       public          postgres    false    221    3493    225            �           2606    16652     EPANDRE EPANDRE_DATE ->DATE_DATE    FK CONSTRAINT     �   ALTER TABLE ONLY public."EPANDRE"
    ADD CONSTRAINT "EPANDRE_DATE ->DATE_DATE" FOREIGN KEY ("DATE") REFERENCES public."DATE"("DATE") NOT VALID;
 N   ALTER TABLE ONLY public."EPANDRE" DROP CONSTRAINT "EPANDRE_DATE ->DATE_DATE";
       public          postgres    false    223    222    3497            �           2606    16647 0   EPANDRE EPANDRE_ID_ENGRAIS -> ENGRAIS_IS_ENGRAIS    FK CONSTRAINT     �   ALTER TABLE ONLY public."EPANDRE"
    ADD CONSTRAINT "EPANDRE_ID_ENGRAIS -> ENGRAIS_IS_ENGRAIS" FOREIGN KEY ("ID_ENGRAIS") REFERENCES public."ENGRAIS"("ID_ENGRAIS") NOT VALID;
 ^   ALTER TABLE ONLY public."EPANDRE" DROP CONSTRAINT "EPANDRE_ID_ENGRAIS -> ENGRAIS_IS_ENGRAIS";
       public          postgres    false    3499    222    225            �           2606    16657 3   EPANDRE EPANDRE_NO_PARCELLE -> PARCELLE_NO_PARCELLE    FK CONSTRAINT     �   ALTER TABLE ONLY public."EPANDRE"
    ADD CONSTRAINT "EPANDRE_NO_PARCELLE -> PARCELLE_NO_PARCELLE" FOREIGN KEY ("NO_PARCELLE") REFERENCES public."PARCELLE"("NO_PARCELLE") NOT VALID;
 a   ALTER TABLE ONLY public."EPANDRE" DROP CONSTRAINT "EPANDRE_NO_PARCELLE -> PARCELLE_NO_PARCELLE";
       public          postgres    false    222    3489    218            �           2606    16697 @   POSSEDER POSSEDER_CODE_ELEMENT -> ELEMENT_CHIMIQUES_CODE_ELEMENT    FK CONSTRAINT     �   ALTER TABLE ONLY public."POSSEDER"
    ADD CONSTRAINT "POSSEDER_CODE_ELEMENT -> ELEMENT_CHIMIQUES_CODE_ELEMENT" FOREIGN KEY ("CODE_ELEMENT") REFERENCES public."ELEMENT_CHIMIQUES"("CODE_ELEMENT") NOT VALID;
 n   ALTER TABLE ONLY public."POSSEDER" DROP CONSTRAINT "POSSEDER_CODE_ELEMENT -> ELEMENT_CHIMIQUES_CODE_ELEMENT";
       public          postgres    false    227    226    3503            �           2606    16667 2   POSSEDER POSSEDER_ID_ENGRAIS -> ENGRAIS_ID_ENGRAIS    FK CONSTRAINT     �   ALTER TABLE ONLY public."POSSEDER"
    ADD CONSTRAINT "POSSEDER_ID_ENGRAIS -> ENGRAIS_ID_ENGRAIS" FOREIGN KEY ("ID_ENGRAIS") REFERENCES public."ENGRAIS"("ID_ENGRAIS") NOT VALID;
 `   ALTER TABLE ONLY public."POSSEDER" DROP CONSTRAINT "POSSEDER_ID_ENGRAIS -> ENGRAIS_ID_ENGRAIS";
       public          postgres    false    3499    226    225            �           2606    16677 $   PRODUCTION PRODUCTION_UN -> UNITE_UN    FK CONSTRAINT     �   ALTER TABLE ONLY public."PRODUCTION"
    ADD CONSTRAINT "PRODUCTION_UN -> UNITE_UN" FOREIGN KEY ("UN") REFERENCES public."UNITE"("UN") NOT VALID;
 R   ALTER TABLE ONLY public."PRODUCTION" DROP CONSTRAINT "PRODUCTION_UN -> UNITE_UN";
       public          postgres    false    3493    220    221            J      x������ � �      Q      x������ � �      U      x������ � �      S      x������ � �      P      x������ � �      V      x������ � �      L      x������ � �      T      x������ � �      N      x������ � �      O      x������ � �     