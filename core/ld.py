import urllib.parse as urllib_parse

from pyld import jsonld
from pyld.jsonld import JsonLdError

schemas = {
    "www.w3.org/ns/activitystreams": {
        "contentType": "application/ld+json",
        "documentUrl": "http://www.w3.org/ns/activitystreams",
        "contextUrl": None,
        "document": {
            "@context": {
                "@vocab": "_:",
                "xsd": "http://www.w3.org/2001/XMLSchema#",
                "as": "https://www.w3.org/ns/activitystreams#",
                "ldp": "http://www.w3.org/ns/ldp#",
                "vcard": "http://www.w3.org/2006/vcard/ns#",
                "id": "@id",
                "type": "@type",
                "Accept": "as:Accept",
                "Activity": "as:Activity",
                "IntransitiveActivity": "as:IntransitiveActivity",
                "Add": "as:Add",
                "Announce": "as:Announce",
                "Application": "as:Application",
                "Arrive": "as:Arrive",
                "Article": "as:Article",
                "Audio": "as:Audio",
                "Block": "as:Block",
                "Collection": "as:Collection",
                "CollectionPage": "as:CollectionPage",
                "Relationship": "as:Relationship",
                "Create": "as:Create",
                "Delete": "as:Delete",
                "Dislike": "as:Dislike",
                "Document": "as:Document",
                "Event": "as:Event",
                "Follow": "as:Follow",
                "Flag": "as:Flag",
                "Group": "as:Group",
                "Ignore": "as:Ignore",
                "Image": "as:Image",
                "Invite": "as:Invite",
                "Join": "as:Join",
                "Leave": "as:Leave",
                "Like": "as:Like",
                "Link": "as:Link",
                "Mention": "as:Mention",
                "Note": "as:Note",
                "Object": "as:Object",
                "Offer": "as:Offer",
                "OrderedCollection": "as:OrderedCollection",
                "OrderedCollectionPage": "as:OrderedCollectionPage",
                "Organization": "as:Organization",
                "Page": "as:Page",
                "Person": "as:Person",
                "Place": "as:Place",
                "Profile": "as:Profile",
                "Question": "as:Question",
                "Reject": "as:Reject",
                "Remove": "as:Remove",
                "Service": "as:Service",
                "TentativeAccept": "as:TentativeAccept",
                "TentativeReject": "as:TentativeReject",
                "Tombstone": "as:Tombstone",
                "Undo": "as:Undo",
                "Update": "as:Update",
                "Video": "as:Video",
                "View": "as:View",
                "Listen": "as:Listen",
                "Read": "as:Read",
                "Move": "as:Move",
                "Travel": "as:Travel",
                "IsFollowing": "as:IsFollowing",
                "IsFollowedBy": "as:IsFollowedBy",
                "IsContact": "as:IsContact",
                "IsMember": "as:IsMember",
                "subject": {"@id": "as:subject", "@type": "@id"},
                "relationship": {"@id": "as:relationship", "@type": "@id"},
                "actor": {"@id": "as:actor", "@type": "@id"},
                "attributedTo": {"@id": "as:attributedTo", "@type": "@id"},
                "attachment": {"@id": "as:attachment", "@type": "@id"},
                "bcc": {"@id": "as:bcc", "@type": "@id"},
                "bto": {"@id": "as:bto", "@type": "@id"},
                "cc": {"@id": "as:cc", "@type": "@id"},
                "context": {"@id": "as:context", "@type": "@id"},
                "current": {"@id": "as:current", "@type": "@id"},
                "first": {"@id": "as:first", "@type": "@id"},
                "generator": {"@id": "as:generator", "@type": "@id"},
                "icon": {"@id": "as:icon", "@type": "@id"},
                "image": {"@id": "as:image", "@type": "@id"},
                "inReplyTo": {"@id": "as:inReplyTo", "@type": "@id"},
                "items": {"@id": "as:items", "@type": "@id"},
                "instrument": {"@id": "as:instrument", "@type": "@id"},
                "orderedItems": {
                    "@id": "as:items",
                    "@type": "@id",
                    "@container": "@list",
                },
                "last": {"@id": "as:last", "@type": "@id"},
                "location": {"@id": "as:location", "@type": "@id"},
                "next": {"@id": "as:next", "@type": "@id"},
                "object": {"@id": "as:object", "@type": "@id"},
                "oneOf": {"@id": "as:oneOf", "@type": "@id"},
                "anyOf": {"@id": "as:anyOf", "@type": "@id"},
                "closed": {"@id": "as:closed", "@type": "xsd:dateTime"},
                "origin": {"@id": "as:origin", "@type": "@id"},
                "accuracy": {"@id": "as:accuracy", "@type": "xsd:float"},
                "prev": {"@id": "as:prev", "@type": "@id"},
                "preview": {"@id": "as:preview", "@type": "@id"},
                "replies": {"@id": "as:replies", "@type": "@id"},
                "result": {"@id": "as:result", "@type": "@id"},
                "audience": {"@id": "as:audience", "@type": "@id"},
                "partOf": {"@id": "as:partOf", "@type": "@id"},
                "tag": {"@id": "as:tag", "@type": "@id"},
                "target": {"@id": "as:target", "@type": "@id"},
                "to": {"@id": "as:to", "@type": "@id"},
                "url": {"@id": "as:url", "@type": "@id"},
                "altitude": {"@id": "as:altitude", "@type": "xsd:float"},
                "content": "as:content",
                "contentMap": {"@id": "as:content", "@container": "@language"},
                "name": "as:name",
                "nameMap": {"@id": "as:name", "@container": "@language"},
                "duration": {"@id": "as:duration", "@type": "xsd:duration"},
                "endTime": {"@id": "as:endTime", "@type": "xsd:dateTime"},
                "height": {"@id": "as:height", "@type": "xsd:nonNegativeInteger"},
                "href": {"@id": "as:href", "@type": "@id"},
                "hreflang": "as:hreflang",
                "latitude": {"@id": "as:latitude", "@type": "xsd:float"},
                "longitude": {"@id": "as:longitude", "@type": "xsd:float"},
                "mediaType": "as:mediaType",
                "published": {"@id": "as:published", "@type": "xsd:dateTime"},
                "radius": {"@id": "as:radius", "@type": "xsd:float"},
                "rel": "as:rel",
                "startIndex": {
                    "@id": "as:startIndex",
                    "@type": "xsd:nonNegativeInteger",
                },
                "startTime": {"@id": "as:startTime", "@type": "xsd:dateTime"},
                "summary": "as:summary",
                "summaryMap": {"@id": "as:summary", "@container": "@language"},
                "totalItems": {
                    "@id": "as:totalItems",
                    "@type": "xsd:nonNegativeInteger",
                },
                "units": "as:units",
                "updated": {"@id": "as:updated", "@type": "xsd:dateTime"},
                "width": {"@id": "as:width", "@type": "xsd:nonNegativeInteger"},
                "describes": {"@id": "as:describes", "@type": "@id"},
                "formerType": {"@id": "as:formerType", "@type": "@id"},
                "deleted": {"@id": "as:deleted", "@type": "xsd:dateTime"},
                "inbox": {"@id": "ldp:inbox", "@type": "@id"},
                "outbox": {"@id": "as:outbox", "@type": "@id"},
                "following": {"@id": "as:following", "@type": "@id"},
                "followers": {"@id": "as:followers", "@type": "@id"},
                "streams": {"@id": "as:streams", "@type": "@id"},
                "preferredUsername": "as:preferredUsername",
                "endpoints": {"@id": "as:endpoints", "@type": "@id"},
                "uploadMedia": {"@id": "as:uploadMedia", "@type": "@id"},
                "proxyUrl": {"@id": "as:proxyUrl", "@type": "@id"},
                "liked": {"@id": "as:liked", "@type": "@id"},
                "oauthAuthorizationEndpoint": {
                    "@id": "as:oauthAuthorizationEndpoint",
                    "@type": "@id",
                },
                "oauthTokenEndpoint": {"@id": "as:oauthTokenEndpoint", "@type": "@id"},
                "provideClientKey": {"@id": "as:provideClientKey", "@type": "@id"},
                "signClientKey": {"@id": "as:signClientKey", "@type": "@id"},
                "sharedInbox": {"@id": "as:sharedInbox", "@type": "@id"},
                "Public": {"@id": "as:Public", "@type": "@id"},
                "source": "as:source",
                "likes": {"@id": "as:likes", "@type": "@id"},
                "shares": {"@id": "as:shares", "@type": "@id"},
                "alsoKnownAs": {"@id": "as:alsoKnownAs", "@type": "@id"},
            }
        },
    },
    "w3id.org/security/v1": {
        "contentType": "application/ld+json",
        "documentUrl": "http://w3id.org/security/v1",
        "contextUrl": None,
        "document": {
            "@context": {
                "id": "@id",
                "type": "@type",
                "dc": "http://purl.org/dc/terms/",
                "sec": "https://w3id.org/security#",
                "xsd": "http://www.w3.org/2001/XMLSchema#",
                "EcdsaKoblitzSignature2016": "sec:EcdsaKoblitzSignature2016",
                "Ed25519Signature2018": "sec:Ed25519Signature2018",
                "EncryptedMessage": "sec:EncryptedMessage",
                "GraphSignature2012": "sec:GraphSignature2012",
                "LinkedDataSignature2015": "sec:LinkedDataSignature2015",
                "LinkedDataSignature2016": "sec:LinkedDataSignature2016",
                "CryptographicKey": "sec:Key",
                "authenticationTag": "sec:authenticationTag",
                "canonicalizationAlgorithm": "sec:canonicalizationAlgorithm",
                "cipherAlgorithm": "sec:cipherAlgorithm",
                "cipherData": "sec:cipherData",
                "cipherKey": "sec:cipherKey",
                "created": {"@id": "dc:created", "@type": "xsd:dateTime"},
                "creator": {"@id": "dc:creator", "@type": "@id"},
                "digestAlgorithm": "sec:digestAlgorithm",
                "digestValue": "sec:digestValue",
                "domain": "sec:domain",
                "encryptionKey": "sec:encryptionKey",
                "expiration": {"@id": "sec:expiration", "@type": "xsd:dateTime"},
                "expires": {"@id": "sec:expiration", "@type": "xsd:dateTime"},
                "initializationVector": "sec:initializationVector",
                "iterationCount": "sec:iterationCount",
                "nonce": "sec:nonce",
                "normalizationAlgorithm": "sec:normalizationAlgorithm",
                "owner": {"@id": "sec:owner", "@type": "@id"},
                "password": "sec:password",
                "privateKey": {"@id": "sec:privateKey", "@type": "@id"},
                "privateKeyPem": "sec:privateKeyPem",
                "publicKey": {"@id": "sec:publicKey", "@type": "@id"},
                "publicKeyBase58": "sec:publicKeyBase58",
                "publicKeyPem": "sec:publicKeyPem",
                "publicKeyWif": "sec:publicKeyWif",
                "publicKeyService": {"@id": "sec:publicKeyService", "@type": "@id"},
                "revoked": {"@id": "sec:revoked", "@type": "xsd:dateTime"},
                "salt": "sec:salt",
                "signature": "sec:signature",
                "signatureAlgorithm": "sec:signingAlgorithm",
                "signatureValue": "sec:signatureValue",
            }
        },
    },
    "*/schemas/litepub-0.1.jsonld": {
        "contentType": "application/ld+json",
        "documentUrl": "http://w3id.org/security/v1",
        "contextUrl": None,
        "document": {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
                {
                    "Emoji": "toot:Emoji",
                    "Hashtag": "as:Hashtag",
                    "PropertyValue": "schema:PropertyValue",
                    "atomUri": "ostatus:atomUri",
                    "conversation": {"@id": "ostatus:conversation", "@type": "@id"},
                    "discoverable": "toot:discoverable",
                    "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
                    "capabilities": "litepub:capabilities",
                    "ostatus": "http://ostatus.org#",
                    "schema": "http://schema.org#",
                    "toot": "http://joinmastodon.org/ns#",
                    "misskey": "https://misskey-hub.net/ns#",
                    "fedibird": "http://fedibird.com/ns#",
                    "value": "schema:value",
                    "sensitive": "as:sensitive",
                    "litepub": "http://litepub.social/ns#",
                    "invisible": "litepub:invisible",
                    "directMessage": "litepub:directMessage",
                    "listMessage": {"@id": "litepub:listMessage", "@type": "@id"},
                    "quoteUrl": "as:quoteUrl",
                    "quoteUri": "fedibird:quoteUri",
                    "oauthRegistrationEndpoint": {
                        "@id": "litepub:oauthRegistrationEndpoint",
                        "@type": "@id",
                    },
                    "EmojiReact": "litepub:EmojiReact",
                    "ChatMessage": "litepub:ChatMessage",
                    "alsoKnownAs": {"@id": "as:alsoKnownAs", "@type": "@id"},
                    "vcard": "http://www.w3.org/2006/vcard/ns#",
                    "formerRepresentations": "litepub:formerRepresentations",
                },
            ]
        },
    },
}


def builtin_document_loader(url: str, options={}):
    # Get URL without scheme
    pieces = urllib_parse.urlparse(url)
    if pieces.hostname is None:
        raise JsonLdError(
            f"No schema built-in for {url!r}",
            "jsonld.LoadDocumentError",
            code="loading document failed",
            cause="NoHostnameError",
        )
    key = pieces.hostname + pieces.path.rstrip("/")
    try:
        return schemas[key]
    except KeyError:
        try:
            key = "*" + pieces.path.rstrip("/")
            return schemas[key]
        except KeyError:
            raise JsonLdError(
                f"No schema built-in for {key!r}",
                "jsonld.LoadDocumentError",
                code="loading document failed",
                cause="KeyError",
            )


def canonicalise(json_data, include_security=False):
    """
    Given an ActivityPub JSON-LD document, round-trips it through the LD
    systems to end up in a canonicalised, compacted format.

    For most well-structured incoming data this won't actually do anything,
    but it's probably good to abide by the spec.
    """
    if not isinstance(json_data, (dict, list)):
        raise ValueError("Pass decoded JSON data into LDDocument")
    return jsonld.compact(
        jsonld.expand(json_data),
        (
            [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
            ]
            if include_security
            else "https://www.w3.org/ns/activitystreams"
        ),
    )
