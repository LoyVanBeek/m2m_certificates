#! /usr/bin/env python3

# Auto-generated by asn1ate v.0.5.1.dev from M2M-Certificate-Definition.asn1
# (last modified on 2016-07-08 14:43:12.164589)

from pyasn1.type import univ, char, namedtype, namedval, tag, constraint, useful
from pyasn1.codec.der import encoder as der_encoder
from binascii import hexlify


class AttributeValue(univ.Choice):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('country',
                            char.PrintableString().subtype(subtypeSpec=constraint.ValueSizeConstraint(2, 2)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('organization',
                            char.UTF8String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('organizationalUnit',
                            char.UTF8String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('distinguishedNameQualifier',
                            char.PrintableString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('stateOrProvince',
                            char.UTF8String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 4)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('locality',
                            char.UTF8String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.NamedType('commonName',
                            char.UTF8String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.NamedType('serialNumber',
                            char.PrintableString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.NamedType('domainComponent',
                            char.IA5String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.NamedType('registeredId', univ.ObjectIdentifier().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.NamedType('octetsName',
                            univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 8)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10)))
    )

    def __init__(self, country=None, 
        organization=None, organizationalUnit=None, 
        distinguishedNameQualifier=None, 
        stateOrProvince=None, locality=None, 
        commonName=None, serialNumber=None, 
        domainComponent=None, 
        registeredId=None, octetsName=None):
        super(AttributeValue, self).__init__()

        values = [country, organization, organizationalUnit, distinguishedNameQualifier, stateOrProvince, locality, commonName, serialNumber, domainComponent, registeredId, octetsName]
        if len([value for value in values if value != None]) > 1:
            raise ValueError("AttributeValue is a Choice, supply only 1 argument")

        if country:
            self['country'] = char.PrintableString(country).subtype(subtypeSpec=constraint.ValueSizeConstraint(2, 2)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        if organization:
            self['organization'] = char.UTF8String(organization).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        if organizationalUnit:
            self['organizationalUnit'] = char.UTF8String(organizationalUnit).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        if distinguishedNameQualifier:
            self['distinguishedNameQualifier'] = char.PrintableString(distinguishedNameQualifier).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        if stateOrProvince:
            self['stateOrProvince'] = char.UTF8String(stateOrProvince).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 4)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        if locality:
            self['locality'] = char.UTF8String(locality).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        if commonName:
            self['commonName'] = char.UTF8String(commonName).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        if serialNumber:
            self['serialNumber'] = char.PrintableString(serialNumber).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))
        if domainComponent:
            self['domainComponent'] = char.IA5String(domainComponent).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))
        if registeredId:
            self['registeredId'] = univ.ObjectIdentifier(registeredId).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))
        if octetsName:
            self['octetsName'] = univ.OctetString(octetsName).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 8)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))

    @staticmethod
    def new(*args, **kwargs):
        return AttributeValue(*args, **kwargs)


class Name(univ.SequenceOf):
    componentType = AttributeValue()
    subtypeSpec=constraint.ValueSizeConstraint(1, 4)

    @staticmethod
    def new(*items):
        if len(items) < Name.subtypeSpec.start:
            raise ValueError("Too few items: need at least {min}".format(min=Name.subtypeSpec.start))
        if len(items) > Name.subtypeSpec.stop:
            raise ValueError("Too many items: can accept at most {max}".format(max=Name.subtypeSpec.stop))

        name = Name()
        for i, item in enumerate(items):
            name[i] = item

        return name


class GeneralName(univ.Choice):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('rfc822Name',
                            char.IA5String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 128)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('dNSName',
                            char.IA5String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 128)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('directoryName', Name()),
        namedtype.NamedType('uniformResourceIdentifier',
                            char.IA5String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 128)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('iPAddress',
                            univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 16)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('registeredID', univ.ObjectIdentifier().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))
    )

    @staticmethod
    def new(rfc822Name=None, dNSName=None, directoryName=None, uniformResourceIdentifier=None, iPAddress=None, registeredID=None):
        general_name = GeneralName()

        if rfc822Name:
            general_name['rfc822Name'] = char.IA5String(rfc822Name).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 128)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        if dNSName:
            general_name['dNSName'] = char.IA5String(dNSName).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 128)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        if directoryName:
            general_name['directoryName'] = directoryName # Name(directoryName).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        if uniformResourceIdentifier:
            general_name['uniformResourceIdentifier'] = char.IA5String(uniformResourceIdentifier).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 128)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        if iPAddress:
            general_name['iPAddress'] = univ.OctetString(iPAddress).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 16)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        if registeredID:
            general_name['registeredID'] = univ.ObjectIdentifier(registeredID).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))

        return general_name


class AuthKeyId(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.OptionalNamedType('keyIdentifier', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('authCertIssuer', GeneralName().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
        namedtype.OptionalNamedType('authCertSerialNum', univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 20)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))
    )

    @staticmethod
    def new(keyIdentifier=None, authCertIssuer=None, authCertSerialNum=None):
        authKeyId = AuthKeyId().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))
        if keyIdentifier:
            octet_string_subtype = univ.OctetString(value=keyIdentifier).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
            # der_encoder.encode(octet_string_subtype)
            authKeyId['keyIdentifier'] = octet_string_subtype
        if authCertIssuer:
            cert_issuer_subtype = authCertIssuer#.subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))
            der_encoder.encode(cert_issuer_subtype)
            authKeyId['authCertIssuer'] = cert_issuer_subtype
        if authCertSerialNum:
            octet_string_subtype2 = univ.OctetString(value=authCertSerialNum).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 20)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
            # der_encoder.encode(octet_string_subtype2)
            authKeyId['authCertSerialNum'] = octet_string_subtype2

        return authKeyId


class Extension(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('extnID', univ.ObjectIdentifier().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.DefaultedNamedType('criticality', univ.Boolean().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)).subtype(value=0)),
        namedtype.NamedType('extnValue', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))
    )

    @staticmethod
    def new(extnID, criticality, extnValue):
        extension = Extension()
        extension['extnID'] = univ.ObjectIdentifier(extnID).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        extension['criticality'] = univ.Boolean(criticality).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)).subtype(value=0)
        extension['extnValue'] = univ.OctetString(extnValue).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))

        return extension


class X509Extensions(univ.SequenceOf):
    componentType = Extension()

    @staticmethod
    def new(*items):
        x509exts = X509Extensions()
        for i, item in enumerate(items):
            x509exts[i] = item

        return x509exts


class TBSCertificate(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.DefaultedNamedType('version', univ.Integer(namedValues=namedval.NamedValues(('v1', 0))).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)).subtype(value='v1')),
        namedtype.NamedType('serialNumber', univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 20)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('cAAlgorithm', univ.ObjectIdentifier().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('cAAlgParams', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('issuer', Name().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('validFrom', univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 5)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('validDuration', univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 4)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.NamedType('subject', Name().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('pKAlgorithm', univ.ObjectIdentifier().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('pKAlgParams', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('pubKey', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('authKeyId', AuthKeyId().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
        namedtype.OptionalNamedType('subjKeyId', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.OptionalNamedType('keyUsage', univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 1)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('basicConstraints', univ.Integer().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))),
        namedtype.OptionalNamedType('certificatePolicy', univ.ObjectIdentifier().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 15))),
        namedtype.OptionalNamedType('subjectAltName', GeneralName().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
        namedtype.OptionalNamedType('issuerAltName', GeneralName().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
        namedtype.OptionalNamedType('extendedKeyUsage', univ.ObjectIdentifier().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 18))),
        namedtype.OptionalNamedType('authInfoAccessOCSP', char.IA5String().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 19))),
        namedtype.OptionalNamedType('cRLDistribPointURI', char.IA5String().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 20))),
        namedtype.OptionalNamedType('x509extensions', X509Extensions().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 21)))
    )

    @staticmethod
    def new(version, serialNumber, 
            subject, 
            cAAlgorithm=None, cAAlgParams=None, 
            issuer=None, 
            validFrom=None, validDuration=None, 
            pKAlgorithm=None, pKAlgParams=None, 
            pubKey=None, authKeyId=None, subjKeyId=None, keyUsage=None, basicConstraints=None, certificatePolicy=None, 
            subjectAltName=None, issuerAltName=None, 
            extendedKeyUsage=None, authInfoAccessOCSP=None, cRLDistribPointURI=None, 
            x509extensions=None):
        tbs = TBSCertificate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))

        tbs['version'] = univ.Integer(value=version, namedValues=namedval.NamedValues(('v1', 0))).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)).subtype(value='v1')
        tbs['serialNumber'] = univ.OctetString(serialNumber).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 20)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        if cAAlgorithm: tbs['cAAlgorithm'] = univ.ObjectIdentifier(cAAlgorithm).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        if cAAlgParams: tbs['cAAlgParams'] = univ.OctetString(cAAlgParams).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        if issuer: tbs['issuer'] = issuer.subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        if validFrom: tbs['validFrom'] = univ.OctetString(validFrom).subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 5)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        if validDuration: tbs['validDuration'] = univ.OctetString(validDuration).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 4)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        tbs['subject'] = subject.subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))
        if pKAlgorithm: tbs['pKAlgorithm'] = univ.ObjectIdentifier(pKAlgorithm).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))
        if pKAlgParams: tbs['pKAlgParams'] = univ.OctetString(pKAlgParams).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))
        if pubKey: tbs['pubKey'] = univ.OctetString(pubKey).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        if authKeyId: tbs['authKeyId'] = authKeyId.subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))
        if subjKeyId: tbs['subjKeyId'] = univ.OctetString(subjKeyId).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))
        if keyUsage: tbs['keyUsage'] = univ.OctetString(keyUsage).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 1)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        if basicConstraints: tbs['basicConstraints'] = univ.Integer(basicConstraints).subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7)).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))
        if certificatePolicy: tbs['certificatePolicy'] = univ.ObjectIdentifier(certificatePolicy).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 15))
        if subjectAltName: tbs['subjectAltName'] = subjectAltName.subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))
        if issuerAltName: tbs['issuerAltName'] = issuerAltName.subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))
        if extendedKeyUsage: tbs['extendedKeyUsage'] = univ.ObjectIdentifier(extendedKeyUsage).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 18))
        if authInfoAccessOCSP: tbs['authInfoAccessOCSP'] = char.IA5String(authInfoAccessOCSP).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 19))
        if cRLDistribPointURI: tbs['cRLDistribPointURI'] = char.IA5String(cRLDistribPointURI).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 20))
        if x509extensions: tbs['x509extensions'] = x509extensions.subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 21))
        return tbs



class Certificate(univ.Sequence):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 20))
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('tbsCertificate', TBSCertificate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
        namedtype.NamedType('cACalcValue', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))
    )

    @staticmethod
    def new(tbsCertificate, cACalcValue):
        certificate = Certificate()
        certificate['tbsCertificate'] = tbsCertificate
        certificate['cACalcValue'] = cACalcValue.subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))

        return certificate

if __name__ == '__main__':
    issuer = Name.new(AttributeValue(country='US'),
                      AttributeValue(organization='Big CAhuna burger'),
                      AttributeValue(locality='Los Angeles'),
                      AttributeValue(serialNumber='987654321'))
    der_encoder.encode(issuer)

    issuerAlternativeName = GeneralName.new(directoryName=issuer)
    der_encoder.encode(issuerAlternativeName)

    subject = Name.new(AttributeValue(country='US'),
                       AttributeValue(organization='ACME corp.'),
                       AttributeValue(stateOrProvince='Utah'),
                       AttributeValue(serialNumber='123456789'))
    der_encoder.encode(subject)

    subjectAlternativeName = GeneralName.new(directoryName=subject)
    # print(subjectAlternativeName.prettyPrint())
    der_encoder.encode(subjectAlternativeName)

    authkey = AuthKeyId.new(keyIdentifier=int(123456789).to_bytes(4, byteorder='big'),
                            #authCertIssuer=subjectAlternativeName,
                            authCertSerialNum=int(123456789).to_bytes(4, byteorder='big'))
    print(authkey.prettyPrint())
    # import pudb; pudb.set_trace()
    # break /usr/local/lib/python3.5/dist-packages/pyasn1/type/univ.py:1124
    # break /usr/local/lib/python3.5/dist-packages/pyasn1/codec/ber/encoder.py:324
    der_encoder.encode(authkey)

    tbs = TBSCertificate.new(version=0,
                             serialNumber=int(123456789).to_bytes(4, byteorder='big'),
                             subject=subject,
                             # cAAlgorithm="1.2.3.4",
                             # cAAlgParams=bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                             # issuer=issuer,
                             # validFrom=int(123456789).to_bytes(4, byteorder='big'),
                             # validDuration=int(123456789).to_bytes(4, byteorder='big'),
                             # pKAlgorithm="1.2.3.4",
                             # pKAlgParams="1.2.3.4",
                             # pubKey=int(123456789).to_bytes(4, byteorder='big'),
                             # authKeyId=authkey,
                             # subjKeyId=int(123456789).to_bytes(4, byteorder='big'),
                             # keyUsage=int(0).to_bytes(1, byteorder='big'),
                             # certificatePolicy="2.5.29.3",
                             # subjectAltName=subjectAlternativeName,
                             # issuerAltName=issuerAlternativeName,
                             # extendedKeyUsage="2.5.29.37",
                             # cRLDistribPointURI=u'www.certificatebegone.com/'
                             )
    der_encoder.encode(tbs)

    cACalcValue = univ.OctetString(value=bytes([1,2,3,4]))
    der_encoder.encode(cACalcValue)

    certificate = Certificate.new(tbs, cACalcValue)

    print(certificate.prettyPrint())
    print(hexlify(der_encoder.encode(certificate)))
    print(len(der_encoder.encode(certificate)))