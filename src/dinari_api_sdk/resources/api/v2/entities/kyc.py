# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ....._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v2.entities import KYCDocumentType, kyc_submit_params, kyc_upload_document_params
from .....types.api.v2.entities.kyc_info import KYCInfo
from .....types.api.v2.entities.kyc_data_param import KYCDataParam
from .....types.api.v2.entities.kyc_document_type import KYCDocumentType
from .....types.api.v2.entities.kyc_upload_document_response import KYCUploadDocumentResponse

__all__ = ["KYCResource", "AsyncKYCResource"]


class KYCResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KYCResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#accessing-raw-response-data-eg-headers
        """
        return KYCResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KYCResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#with_streaming_response
        """
        return KYCResourceWithStreamingResponse(self)

    def retrieve(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KYCInfo:
        """
        Get most recent KYC data of the `Entity`.

        If there are any completed KYC checks, data from the most recent one will be
        returned. If there are no completed KYC checks, the most recent KYC check
        information, regardless of status, will be returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            f"/api/v2/entities/{entity_id}/kyc",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYCInfo,
        )

    def submit(
        self,
        entity_id: str,
        *,
        data: KYCDataParam,
        provider_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KYCInfo:
        """
        Submit KYC data directly, for partners that are provisioned to provide their own
        KYC data.

        This feature is available for everyone in sandbox mode, and for specifically
        provisioned partners in production.

        Args:
          data: KYC data for an `Entity`.

          provider_name: Name of the KYC provider that provided the KYC information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            f"/api/v2/entities/{entity_id}/kyc",
            body=maybe_transform(
                {
                    "data": data,
                    "provider_name": provider_name,
                },
                kyc_submit_params.KYCSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYCInfo,
        )

    def upload_document(
        self,
        kyc_id: str,
        *,
        entity_id: str,
        document_type: KYCDocumentType,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KYCUploadDocumentResponse:
        """
        Upload KYC-related documentation for partners that are provisioned to provide
        their own KYC data.

        Args:
          document_type: Type of `KYCDocument` to be uploaded.

          file: File to be uploaded. Must be a valid image or PDF file (jpg, jpeg, png, pdf)
              less than 10MB in size.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        if not kyc_id:
            raise ValueError(f"Expected a non-empty value for `kyc_id` but received {kyc_id!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/api/v2/entities/{entity_id}/kyc/{kyc_id}/document",
            body=maybe_transform(body, kyc_upload_document_params.KYCUploadDocumentParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"document_type": document_type}, kyc_upload_document_params.KYCUploadDocumentParams
                ),
            ),
            cast_to=KYCUploadDocumentResponse,
        )


class AsyncKYCResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKYCResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKYCResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKYCResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#with_streaming_response
        """
        return AsyncKYCResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KYCInfo:
        """
        Get most recent KYC data of the `Entity`.

        If there are any completed KYC checks, data from the most recent one will be
        returned. If there are no completed KYC checks, the most recent KYC check
        information, regardless of status, will be returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            f"/api/v2/entities/{entity_id}/kyc",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYCInfo,
        )

    async def submit(
        self,
        entity_id: str,
        *,
        data: KYCDataParam,
        provider_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KYCInfo:
        """
        Submit KYC data directly, for partners that are provisioned to provide their own
        KYC data.

        This feature is available for everyone in sandbox mode, and for specifically
        provisioned partners in production.

        Args:
          data: KYC data for an `Entity`.

          provider_name: Name of the KYC provider that provided the KYC information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            f"/api/v2/entities/{entity_id}/kyc",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "provider_name": provider_name,
                },
                kyc_submit_params.KYCSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYCInfo,
        )

    async def upload_document(
        self,
        kyc_id: str,
        *,
        entity_id: str,
        document_type: KYCDocumentType,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KYCUploadDocumentResponse:
        """
        Upload KYC-related documentation for partners that are provisioned to provide
        their own KYC data.

        Args:
          document_type: Type of `KYCDocument` to be uploaded.

          file: File to be uploaded. Must be a valid image or PDF file (jpg, jpeg, png, pdf)
              less than 10MB in size.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        if not kyc_id:
            raise ValueError(f"Expected a non-empty value for `kyc_id` but received {kyc_id!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/api/v2/entities/{entity_id}/kyc/{kyc_id}/document",
            body=await async_maybe_transform(body, kyc_upload_document_params.KYCUploadDocumentParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"document_type": document_type}, kyc_upload_document_params.KYCUploadDocumentParams
                ),
            ),
            cast_to=KYCUploadDocumentResponse,
        )


class KYCResourceWithRawResponse:
    def __init__(self, kyc: KYCResource) -> None:
        self._kyc = kyc

        self.retrieve = to_raw_response_wrapper(
            kyc.retrieve,
        )
        self.submit = to_raw_response_wrapper(
            kyc.submit,
        )
        self.upload_document = to_raw_response_wrapper(
            kyc.upload_document,
        )


class AsyncKYCResourceWithRawResponse:
    def __init__(self, kyc: AsyncKYCResource) -> None:
        self._kyc = kyc

        self.retrieve = async_to_raw_response_wrapper(
            kyc.retrieve,
        )
        self.submit = async_to_raw_response_wrapper(
            kyc.submit,
        )
        self.upload_document = async_to_raw_response_wrapper(
            kyc.upload_document,
        )


class KYCResourceWithStreamingResponse:
    def __init__(self, kyc: KYCResource) -> None:
        self._kyc = kyc

        self.retrieve = to_streamed_response_wrapper(
            kyc.retrieve,
        )
        self.submit = to_streamed_response_wrapper(
            kyc.submit,
        )
        self.upload_document = to_streamed_response_wrapper(
            kyc.upload_document,
        )


class AsyncKYCResourceWithStreamingResponse:
    def __init__(self, kyc: AsyncKYCResource) -> None:
        self._kyc = kyc

        self.retrieve = async_to_streamed_response_wrapper(
            kyc.retrieve,
        )
        self.submit = async_to_streamed_response_wrapper(
            kyc.submit,
        )
        self.upload_document = async_to_streamed_response_wrapper(
            kyc.upload_document,
        )
